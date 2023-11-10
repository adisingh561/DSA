import pandas as pd
import geopandas as gpd
import movingpandas as mpd
from shapely.geometry import Point
from datetime import datetime,timedelta,timezone
from algorithms_pt.utils.mysql_connection import mysql_connection
from pyproj import CRS
from itspelogger import Logger
import requests, json
from configparser import ConfigParser
import schedule
import time 
from dateutil import parser
import random
from shapely.ops import nearest_points
from shapely.geometry import LineString


class Distance_reports:
    def __init__(self,logger,confog='config.ini'):
        self.bus_scn = {}
        self.conf = ConfigParser()
        self.conf.read(confog)
        self.logger=logger
        #htms
        conff=trns = self.conf["GPS_ALERT"]
        self.fastapi_host = conff['fastapi_host'] 
        self.htms_port = conff['htms_port']
        self.url = conff['url']
        self.transit_port = conff['transit_port']

        self.transit_url = self.url+self.fastapi_host+":"+self.transit_port
        self.htms_url = self.url + self.fastapi_host + ":" + self.htms_port
        self.logger.debug("Distance report initialised")

    def vehicle_distance_reports(self):
        try:
            db=mysql_connection()
            cursor = db.get_cursor()
            bus_scn = {}
            payload={}
            headers = {}
            # date="2023-10-26"
            # base_url = self.htms_url + f"/pt/bus_gps/get_gps_data?date="+str(date)
            date="2023-11-08"
            db=mysql_connection('htms')
            htms_cursor=db.get_cursor()
            sql="""select * from gps_tracking where date(timestamp)=%s order by timestamp ASC;"""
            htms_cursor.execute(sql,(date,))
            data=htms_cursor.fetchall()
            # print(data)

            # base_url = self.htms_url+"/pt/bus_gps/get_gps_data"
            # response = requests.request("GET",base_url, headers=headers, data=payload)
            # data = json.loads(response.text)
            # print(data)
            if data:
                for data_dict in data:
                    dtt = {}
                    if data_dict['latitude'] !=0 and data_dict['longitude']!=0:
                        dtt['latitude']=data_dict['latitude']
                        dtt['longitude']=data_dict['longitude']
                        dtt['system_code_number']=data_dict['SystemCodeNumber']
                        dtt['timestamp'] =data_dict['timestamp']
                        if dtt["system_code_number"] not in bus_scn:
                            bus_scn[dtt.get("system_code_number")] = []
                            bus_scn[dtt["system_code_number"]].append(dtt)
                        else:
                            bus_scn[dtt["system_code_number"]].append(dtt)
               
                # gdf= gpd.read_file('algorithms_pt/tvm_shape/TVM_FINAL_SHAPE.shp')
                db=mysql_connection()
                cursor = db.get_cursor()
                querry="""select gps_device from pt_block_bus pt INNER JOIN pt_bus_gps_device as pg ON pg.reg_num=pt.reg_num where date(date)=%s;"""
                cursor.execute(querry,(date,))
                assign_bus=cursor.fetchall()
                if assign_bus:
                        assign_bus={x['gps_device'] for x in assign_bus}
                for bus in bus_scn.keys():
                    if bus in assign_bus:
                        dataa=bus_scn[bus]
                        geom,tstamp = [],[]
                        time_stamp = []
                        x = 0
                        nearest_sum=0
                        lati,longi=0,0
                        sum_n=0
                        gdf= gpd.read_file('algorithms_pt/tvm_shape/TVM_FINAL_SHAPE.shp')
                        for element in dataa:
                            date_time = datetime.now() + timedelta(seconds=x)
                            lat = element['latitude']  
                            lon = element['longitude']
                            if lati!=lat or longi!=lon or lati==0 and longi==0:
                                lati=lat
                                longi=lon
                                geom.append(Point(lon,lat))
                                tstamp.append(date_time)
                                time_stamp.append(element['timestamp'])
                                x += 0.5
                                # gdf= gpd.read_file('algorithms_pt/tvm_shape/TVM_FINAL_SHAPE.shp')
                                user_location = Point(lon,lat)
                                # print(" latitude_longitude  : ",lat," : ",lon)
                                gdf = gdf.to_crs(epsg=32644)
                                gdf['distance'] = gdf['geometry'].distance(user_location)
                                nearest_edge = gdf.loc[gdf['distance'].idxmin()]
                                # print("Nereast_Edge  :  ",nearest_edge)
                                # print('geometry  :  ',nearest_edge['geometry'].length)
                                line=nearest_edge['geometry']
                                # is_simple=line.is_simple
                                # print("sum_of_dist  : ",LineString(line).length)
                                sum_f=LineString(line).length
                                ###use to check contigeouse or not
                                if line.is_simple:
                                    sum_n=sum_n+sum_f
                                    
                                    # print("Hiiii  :  contigeous")
                                else:
                                    # sum_n=sum_n+LineString(line).length
                                    intersects = gdf['geometry'].intersects(user_location)
                                    nearest_edges = gdf[intersects]
                                    print('nearest_passed  : ',nearest_edges)
                                    print("Hiiii  :  Not contigeous")

                        time_stamp.sort()
                        
                        date=datetime.strftime(time_stamp[0],"%Y-%m-%d %H:%M:%S")
                        start_time=parser.parse(date)
                        # Dt = parser.parse(time_stamp[-1])
                        ed_data=datetime.strftime(time_stamp[-1],"%Y-%m-%d %H:%M:%S")
                        end_time=parser.parse(ed_data)
                        # Dataframing to calculate distance
                        dataframe = pd.DataFrame()
                        dataframe['geometry'] = geom
                        dataframe['t'] = tstamp
                        dataframe = dataframe.set_index('t')
                        
                        if len(dataframe)>1:
                            gdf = gpd.GeoDataFrame(dataframe,crs = CRS(4326))
                            traj = mpd.Trajectory(gdf,4)
                            # trajectories=mpd.Trajectory(gdf,4)

                            
                            # road_network = gpd.read_file('algorithms_pt/tvm_shape/TVM_FINAL_SHAPE.shp')

                            # trajectory = traj.snap_to_road(road_network, source_crs='EPSG:4326',target_crs='EPSG:4326',snap_distance=0.001)

                            # trajectory = traj.snap_to_nearest_road(road_network, snap_distance=0.001)
                    

                            # trajectories_snapped = traj.snap_to_road(road_network, source_crs='EPSG:4326', target_crs='EPSG:4326', snap_distance=0.001)
                            # distance_covers = round((trajectory.get_length())/1000,2)


                            distance_cover = round((traj.get_length())/1000,2)
                            distance_covers=round((sum_n/1000),2)
                            # ne_distance=round((traj.get_length()+nearest_sum)/1000,2)
                            # print("contigious_dist  : ",round((sum_n/1000),2))
                            print('old_dist : ',distance_cover)
                            print('new_dist : ',distance_covers)
                            # print('new_dist : ',distance_covers+nearest_sum)
                            # print("new_with_traj_dist : ",ne_distance)
                            # return 0
                        else:
                            distance_covers=0      
                        busdata_url = self.transit_url+"/pt/operator/get_bus_type_name/" +bus
                        response = requests.request("GET",busdata_url, headers=headers, data=payload)
                        bus_data = json.loads(response.text)
                            
                        if not bus_data:
                            reg_num="-"
                        else:
                            reg_num=bus_data[0]["reg_num"]
                        scn=bus
                        
                        if end_time!=None and start_time!=None:
                            duration=end_time-start_time
                            duration_operation = duration.total_seconds()//60

                        currentDate = datetime.now() - timedelta(days=1)
                        operation_date = currentDate.strftime('%Y-%m-%d')
                        start_timestamp=start_time.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
                        end_timestamp=end_time.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
                        # print('start',start_timestamp)
                        # print('end',end_timestamp)
                        dic_data={}
                        dic_data['system_code_number']=scn
                        dic_data['registration_number']=reg_num
                        dic_data['distance_covered']=distance_covers
                        dic_data['start_timestamp']= start_timestamp
                        dic_data['end_timestamp']= end_timestamp
                        dic_data['operation_date']=operation_date
                        dic_data['operation_duration']=duration_operation
                        payload={}
                        headers = {}
                        base_url = self.transit_url+"/pt/operator/vehicle_distance_reports"
                        response = requests.request("POST",base_url,headers=headers,json=dic_data)
                        print('Distance_report inserted')
            else:
                print("data not found  : ",date)
        except Exception as ex:
            raise self.logger.debug('Distance data not found %s', ex)


def main(logger):
    vd=Distance_reports(logger)
    vd.vehicle_distance_reports()

# def scheduler():
#     config='config.ini'
#     conf = ConfigParser()
#     logger = Logger("REPORTS_TIME")
#     logger.debug("REPORTS_TIME started")
#     conf.read(config)
#     start_time = str(conf.get("REPORTS_TIME", "distance_time"))
#     schedule.every().day.at(start_time).do(main,logger)
#     while True:
#         schedule.run_pending()
#         time.sleep(10)

def scheduler():
    logger=Logger("started")
    main(logger)
