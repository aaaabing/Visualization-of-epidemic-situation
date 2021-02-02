package com.lzr.Dao;

import org.apache.ibatis.annotations.Param;

import java.util.Date;

public interface CityNovData {
    public Integer getTodayNovCondition(@Param("cityName") String cityName,@Param("date") String date);
    public Integer getTotalNovCondition(@Param("cityName") String cityName,@Param("date") String date);
}
