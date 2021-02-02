package com.lzr.Util;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;


import java.io.IOException;


/**
 * @Auther 刘曾瑞
 * @Version 2020.12.20
 *定时爬取最新的疫情的数据
 */
@Configuration
@EnableScheduling
public class TimerClock {
    private static final Logger logger = LoggerFactory.getLogger(TimerClock.class);
    /*每天凌晨一点更新数据*/
    @Scheduled(cron = "0 0 1 * * ?")
public void DownloadDate(){
        Process process;
        try {
            process= Runtime.getRuntime().exec("python .\\src\\main\\resources\\python\\city_data.py");
            process= Runtime.getRuntime().exec("python .\\src\\main\\resources\\python\\National_data.py");
            process= Runtime.getRuntime().exec("python .\\src\\main\\resources\\python\\Province_data.py");

        } catch (IOException e) {

        }
    }
}
