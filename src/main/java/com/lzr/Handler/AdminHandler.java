package com.lzr.Handler;

import com.lzr.Service.ManageData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;


/**
 * @TDBO   用于传递数据
 * @Author 刘曾瑞
 * @Version 2020.12.20
 */
@Controller
public class AdminHandler {
    @Autowired
    ManageData manageData;
        @GetMapping("/index")
        public String ShowData(){
            return "index";
        }
        @ResponseBody
        @PostMapping("/requestProvinceData")
        public String requestProvinceData(){
            return manageData.getProvidenceData();
        }
        @ResponseBody
        @PostMapping("/requestCityData")
        public String requestCityData(@RequestBody String City){
            return manageData.getCityData(City.replaceAll("\"",""));
        }
        @ResponseBody
        @PostMapping("/requestTotalData")
        public String requestTotalData(){
            return manageData.getTotalProvidenceData();
        }
    @ResponseBody
    @PostMapping("/requestTotalCityData")
    public String requestTotalCityData(@RequestBody String City){
        return manageData.getTotalCityData(City.replaceAll("\"",""));
    }

}
