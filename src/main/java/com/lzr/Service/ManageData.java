package com.lzr.Service;


import com.alibaba.fastjson.JSONObject;
import com.lzr.Dao.CityNovData;
import com.lzr.Dao.ProvinceNovData;
import com.lzr.Entity.DaliyCond;
import com.lzr.Util.getCitiesUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.text.SimpleDateFormat;
import java.util.*;

/**
 * @Author 刘曾瑞
 * @Version 2020.12.27
 */
@Service
public class ManageData {
    private final String date=this.getBJTime().replaceAll("-","");
    @Autowired
    ProvinceNovData provinceNovData;
    @Autowired
    getCitiesUtil getCities;
    @Autowired
    CityNovData cityNovData;
    public String getProvidenceData(){
        List<DaliyCond>daliyConds=new LinkedList<>();
        List<String> provinces=getCities.getProvinces("中国");
        for (String ss:provinces){
            String c=ss.replaceAll("市","");
            c=c.replaceAll("省","");
            c=c.replaceAll("自治区","");
            c=c.replaceAll("回族","");
            c=c.replaceAll("维吾尔","");
            c=c.replaceAll("壮族","");
            daliyConds.add(new DaliyCond(c,provinceNovData.getTodayNovCondition(ss,date)));
        }
       return JSONObject.toJSONString(daliyConds);
    }
    public String getCityData(String City){
        if(City.equals("北京")||City.equals("上海")||City.equals("天津")||City.equals("重庆"))
            City=City+"市";
        else
            if(City.equals("广西"))
                City=City+"壮族自治区";
            else
                if(City.equals("内蒙古")||City.equals("西藏"))
                    City+="自治区";
                else
                    if(City.equals("新疆"))
                        City+="维吾尔自治区";
                    else
                        if(City.equals("宁夏"))
                            City+="回族自治区";
                        else
                            if(!City.equals("香港")&&!City.equals("澳门")&&!City.equals("台湾"))
                                City+="省";


        List<String>cities=getCities.getCities("中国",City);
        List<DaliyCond>daliyConds=new LinkedList<>();
        if (City.equals("北京市")||City.equals("上海市")||City.equals("重庆市")||City.equals("天津市")){

            for (String  ss:cities){
                ss+="区";
                if(cityNovData.getTodayNovCondition(ss,date)!=null)
                    daliyConds.add(new DaliyCond(ss,cityNovData.getTotalNovCondition(ss,date)));
                else daliyConds.add((new DaliyCond(ss,0)));
            }
        }
        else{

            for (String  ss:cities){
                if(cityNovData.getTodayNovCondition(ss,date)!=null)
                    daliyConds.add(new DaliyCond(ss+"市",cityNovData.getTotalNovCondition(ss,date)));
                else daliyConds.add((new DaliyCond(ss+"市",0)));
            }
        }
        return JSONObject.toJSONString(daliyConds);
    }
    public String getTotalProvidenceData(){
        List<DaliyCond>TotalConds=new LinkedList<>();
        List<String> provinces=getCities.getProvinces("中国");
        for (String ss:provinces){
            String c=ss.replaceAll("市","");
            c=c.replaceAll("省","");
            c=c.replaceAll("自治区","");
            c=c.replaceAll("回族","");
            c=c.replaceAll("维吾尔","");
            c=c.replaceAll("壮族","");
            TotalConds.add(new DaliyCond(c,provinceNovData.getTotalNovCondition(ss,date)));
        }
        return JSONObject.toJSONString(TotalConds);
    }
    public String getTotalCityData(String City){
        if(City.equals("北京")||City.equals("上海")||City.equals("天津")||City.equals("重庆"))
            City=City+"市";
        else
        if(City.equals("广西"))
            City=City+"壮族自治区";
        else
        if(City.equals("内蒙古")||City.equals("西藏"))
            City+="自治区";
        else
        if(City.equals("新疆"))
            City+="维吾尔自治区";
        else
        if(City.equals("宁夏"))
            City+="回族自治区";
        else
        if(!City.equals("香港")&&!City.equals("澳门")&&!City.equals("台湾"))
            City+="省";
        List<DaliyCond>TotalConds=new LinkedList<>();
        List<String>cities=getCities.getCities("中国",City);
        if (City.equals("北京市")||City.equals("上海市")||City.equals("重庆市")||City.equals("天津市")){

            for (String  ss:cities){
                ss+="区";
                if(cityNovData.getTotalNovCondition(ss,date)!=null)
                    TotalConds.add(new DaliyCond(ss,cityNovData.getTotalNovCondition(ss,date)));
                else TotalConds.add((new DaliyCond(ss,0)));
            }
        }
        else{

            for (String  ss:cities){
                if(cityNovData.getTotalNovCondition(ss,date)!=null)
                    TotalConds.add(new DaliyCond(ss+"市",cityNovData.getTotalNovCondition(ss,date)));
                else TotalConds.add((new DaliyCond(ss+"市",0)));
            }
        }

        System.out.println(JSONObject.toJSONString(TotalConds));
        return JSONObject.toJSONString(TotalConds);
    }
    private String getBJTime() {

        Date date = new Date();
        SimpleDateFormat bjSdf = new SimpleDateFormat("yyyy-MM-dd");     // 北京
        bjSdf.setTimeZone(TimeZone.getTimeZone("Asia/Shanghai"));  // 设置北京时区
        return bjSdf.format(date);
    }
}
