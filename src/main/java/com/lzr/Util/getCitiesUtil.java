package com.lzr.Util;

import org.dom4j.Document;
import org.dom4j.DocumentException;
import org.dom4j.Element;
import org.dom4j.io.SAXReader;
import org.springframework.stereotype.Component;

import java.io.File;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
/**
 * @Author 刘曾瑞
 * @Version 2020 12.20
 */
@Component
public class getCitiesUtil {


    private static final List<String> COUNTRY_REGION = new ArrayList<String>();
    private SAXReader saxReader;
    private Document document;
    private Element  element;
    private getCitiesUtil(){
    saxReader=new SAXReader();
        try {

            document=saxReader.read(new File("src/main/resources/config/LocList.xml"));
            System.out.println(document);
        } catch (DocumentException e) {
            System.out.println("ERROR");
            e.printStackTrace();

        }
        element=document.getRootElement();
        Iterator iterator=element.elementIterator();
        Element ele =null;
        while (iterator.hasNext()){
            ele=(Element)iterator.next();
            COUNTRY_REGION.add(ele.attributeValue("Name"));
        }
    }
    private List<Element> provinces(String countryName){
        Iterator it =  element.elementIterator();
        List<Element> provinces = new ArrayList<Element>();
        Element ele = null;
        while(it.hasNext()){
            ele = (Element)it.next();
            COUNTRY_REGION.add(ele.attributeValue("Name"));
            if(ele.attributeValue("Name").equals(countryName)){
                provinces = ele.elements();
                break;
            }
        }
        return provinces;
    }
    private List<Element> cities(String countryName, String provinceName){
        List<Element> provinces =  this.provinces(countryName);
        List<Element> cities = new ArrayList<Element>();
        if(provinces==null || provinces.size()==0){     //没有这个城市
            return cities;
        }

        for(int i=0; i<provinces.size(); i++){
            if(provinces.get(i).attributeValue("Name").equals(provinceName)){
                cities = provinces.get(i).elements();
                break;
            }
    }
        return cities;
    }
    public List<String> getCities(String countryName, String provinceName){
        List<Element> tmp =  this.cities(countryName, provinceName);
        List<String> cities = new ArrayList<String>();
        for(int i=0; i<tmp.size(); i++){
            cities.add(tmp.get(i).attributeValue("Name"));
        }
        return cities;
    }
    public List<String> getProvinces(String countryName){
        List<Element> tmp = this.provinces(countryName);
        List<String> list = new ArrayList<String>();
        for(int i=0; i<tmp.size(); i++){
            list.add(tmp.get(i).attributeValue("Name"));
        }
        return list;
    }
}
