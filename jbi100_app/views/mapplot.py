from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
from datetime import datetime

from ..config import visibility_to_code, weather_to_code, type_track_to_code, acc_type_to_code

class Mapplot(html.Div):
    def __init__(self, name, df):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df
        self.center = {'lat': 37.0902, 'lon': -95.7129}
        self.zoom = 3
        self.selected_state = None
        self.filter_data(None, 
                         None, 
                         None, 
                         None,
                         None, 
                         None, 
                         None,
                         None,
                         None, 
                         None, 
                         None, 
                         None,
                         None,
                         None, 
                         None, 
                         None, 
                         None,
                         None, 
                         None,
                         None,
                         None, 
                         None)
        self.fig = self.get_figure()

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="graph_card",
            children=[
                dcc.Loading(
                    id="loading-map",
                    type="default",
                    delay_show=0,
                    delay_hide=0,
                    children=dcc.Graph(id=self.html_id, figure=self.fig, config={"scrollZoom": True, "displayModeBar": True })
                ),
                
            ],
        )

    def filter_data(self, 
                    selected_points,
                    selected_state,
                    selected_weather, 
                    selected_visibility, 
                    selected_temperature,
                    selected_train_track, 
                    selected_acc_type, 
                    selected_train_speed,
                    selected_tons,
                    selected_equipment_damage,
                    selected_track_damage,
                    selected_reportable_damage,
                    selected_people_killed,
                    selected_people_injured,
                    selected_personel_duty,
                    selected_engineers_duty,
                    selected_firemen_duty,
                    selected_conductors_duty,
                    selected_brakemen_duty,
                    selected_start_date, 
                    selected_end_date, 
                    selected_time):
        
        self.filtered_data = self.df[self.df['location_substituded'] == False].copy()

        if selected_points is not None:
            self.filtered_data['show'] = False
            self.filtered_data['reason'] = 'select'

            curr_ids = [point['customdata'][0] for point in selected_points['points']]
            
            for point_id in curr_ids:
                self.filtered_data.loc[point_id, 'show'] = True

        if selected_state is not None:
            self.filtered_data.loc[self.filtered_data['STATE'] != selected_state, 'show'] = False
            self.filtered_data.loc[self.filtered_data['STATE'] != selected_state, 'reason'] = 'state'

        if selected_weather is not None:
            self.filtered_data.loc[self.filtered_data['WEATHER'] != weather_to_code.get(selected_weather), 'show'] = False
            self.filtered_data.loc[self.filtered_data['WEATHER'] != weather_to_code.get(selected_weather), 'reason'] = 'weather'

        if selected_visibility is not None:
            self.filtered_data.loc[self.filtered_data['VISIBLTY'] != visibility_to_code.get(selected_visibility), 'show'] = False
            self.filtered_data.loc[self.filtered_data['VISIBLTY'] != visibility_to_code.get(selected_visibility), 'reason'] = 'visibility'

        if selected_temperature is not None:
            start_temperature = selected_temperature[0]
            end_temperature = selected_temperature[1]
            self.filtered_data.loc[self.filtered_data['TEMP'] < start_temperature, 'show'] = False
            self.filtered_data.loc[self.filtered_data['TEMP'] > end_temperature, 'show'] = False
            
            self.filtered_data.loc[self.filtered_data['TEMP'] < start_temperature, 'reason'] = 'start temperature'
            self.filtered_data.loc[self.filtered_data['TEMP'] > end_temperature, 'reason'] = 'end temperature'

        if selected_train_track is not None:
            self.filtered_data.loc[self.filtered_data['TYPTRK'] != type_track_to_code.get(selected_train_track), 'show'] = False
            self.filtered_data.loc[self.filtered_data['TYPTRK'] != type_track_to_code.get(selected_train_track), 'reason'] = 'track type'
        
        if selected_acc_type is not None:
            self.filtered_data.loc[self.filtered_data['TYPE'] != acc_type_to_code.get(selected_acc_type), 'show'] = False
            self.filtered_data.loc[self.filtered_data['TYPE'] != acc_type_to_code.get(selected_acc_type), 'reason'] = 'accident type'

        if selected_train_speed is not None:
            start_train_speed = selected_train_speed[0]
            end_train_speed = selected_train_speed[1]
            self.filtered_data.loc[self.filtered_data['TRNSPD'] < start_train_speed, 'show'] = False
            self.filtered_data.loc[self.filtered_data['TRNSPD'] > end_train_speed, 'show'] = False
            
            self.filtered_data.loc[self.filtered_data['TRNSPD'] < start_train_speed, 'reason'] = 'start train speed'
            self.filtered_data.loc[self.filtered_data['TRNSPD'] > end_train_speed, 'reason'] = 'end train speed'

        if selected_tons is not None:
            start_tons = selected_tons[0]
            end_tons = selected_tons[1]
            self.filtered_data.loc[self.filtered_data['TONS'] < start_tons, 'show'] = False
            self.filtered_data.loc[self.filtered_data['TONS'] > end_tons, 'show'] = False
            
            self.filtered_data.loc[self.filtered_data['TONS'] < start_tons, 'reason'] = 'start tons'
            self.filtered_data.loc[self.filtered_data['TONS'] > end_tons, 'reason'] = 'end tons'

        if selected_equipment_damage is not None:
            start_equipment_damage = selected_equipment_damage[0]
            end_equipment_damage = selected_equipment_damage[1]
            self.filtered_data.loc[self.filtered_data['EQPDMG'] < start_equipment_damage, 'show'] = False
            self.filtered_data.loc[self.filtered_data['EQPDMG'] > end_equipment_damage, 'show'] = False
            
            self.filtered_data.loc[self.filtered_data['EQPDMG'] < start_equipment_damage, 'reason'] = 'start equipment damage'
            self.filtered_data.loc[self.filtered_data['EQPDMG'] > end_equipment_damage, 'reason'] = 'end equipment damage'

        if selected_track_damage is not None:
            start_track_damage = selected_track_damage[0]
            end_track_damage = selected_track_damage[1]
            self.filtered_data.loc[self.filtered_data['TRKDMG'] < start_track_damage, 'show'] = False
            self.filtered_data.loc[self.filtered_data['TRKDMG'] > end_track_damage, 'show'] = False
            
            self.filtered_data.loc[self.filtered_data['TRKDMG'] < start_track_damage, 'reason'] = 'start track damage'
            self.filtered_data.loc[self.filtered_data['TRKDMG'] > end_track_damage, 'reason'] = 'end track damage'

        if selected_reportable_damage is not None:
            start_reportable_damage = selected_reportable_damage[0]
            end_reportable_damage = selected_reportable_damage[1]
            self.filtered_data.loc[self.filtered_data['ACCDMG'] < start_reportable_damage, 'show'] = False
            self.filtered_data.loc[self.filtered_data['ACCDMG'] > end_reportable_damage, 'show'] = False
            
            self.filtered_data.loc[self.filtered_data['ACCDMG'] < start_reportable_damage, 'reason'] = 'start reportable damage'
            self.filtered_data.loc[self.filtered_data['ACCDMG'] > end_reportable_damage, 'reason'] = 'end reportable damage'

        if selected_people_killed is not None:
            self.filtered_data.loc[self.filtered_data['CASKLDRR'] != int(selected_people_killed), 'show'] = False
            self.filtered_data.loc[self.filtered_data['CASKLDRR'] != int(selected_people_killed), 'reason'] = 'people killed'

        if selected_people_injured is not None:
            self.filtered_data.loc[self.filtered_data['CASINJRR'] != int(selected_people_injured), 'show'] = False
            self.filtered_data.loc[self.filtered_data['CASINJRR'] != int(selected_people_injured), 'reason'] = 'people injured'

        if selected_personel_duty is not None:
            self.filtered_data.loc[self.filtered_data['personel'] != float(selected_personel_duty), 'show'] = False
            self.filtered_data.loc[self.filtered_data['personel'] != float(selected_personel_duty), 'reason'] = 'personel on duty'

        if selected_engineers_duty is not None:
            self.filtered_data.loc[self.filtered_data['ENGRS'] != float(selected_engineers_duty), 'show'] = False
            self.filtered_data.loc[self.filtered_data['ENGRS'] != float(selected_engineers_duty), 'reason'] = 'engineers on duty'

        if selected_firemen_duty is not None:
            self.filtered_data.loc[self.filtered_data['FIREMEN'] != float(selected_firemen_duty), 'show'] = False
            self.filtered_data.loc[self.filtered_data['FIREMEN'] != float(selected_firemen_duty), 'reason'] = 'firemen on duty'

        if selected_conductors_duty is not None:
            self.filtered_data.loc[self.filtered_data['CONDUCTR'] != float(selected_conductors_duty), 'show'] = False
            self.filtered_data.loc[self.filtered_data['CONDUCTR'] != float(selected_conductors_duty), 'reason'] = 'conductors on duty'

        if selected_brakemen_duty is not None:
            self.filtered_data.loc[self.filtered_data['BRAKEMEN'] != float(selected_brakemen_duty), 'show'] = False
            self.filtered_data.loc[self.filtered_data['BRAKEMEN'] != float(selected_brakemen_duty), 'reason'] = 'brakemen on duty'

        # if selected_start_date != None and selected_end_date != None:
        #     print(selected_start_date.strip(), selected_end_date.strip())
        #     print('-'+selected_start_date.strip()+'-')

        if selected_start_date is not None:
            curr_date = datetime.strptime(selected_start_date.strip(), '%Y-%m-%d')
            self.filtered_data.loc[self.filtered_data['YEAR4'] < curr_date.year, 'show'] = False
            self.filtered_data.loc[((self.filtered_data['YEAR4'] == curr_date.year) & (self.filtered_data['MONTH'] < curr_date.month)), 'show'] = False
            self.filtered_data.loc[((self.filtered_data['YEAR4'] == curr_date.year) & (self.filtered_data['MONTH'] == curr_date.month) & (self.filtered_data['DAY'] < curr_date.day)), 'show'] = False

            self.filtered_data.loc[self.filtered_data['YEAR4'] < curr_date.year, 'reason'] = 'start date'
            self.filtered_data.loc[((self.filtered_data['YEAR4'] == curr_date.year) & (self.filtered_data['MONTH'] < curr_date.month)), 'reason'] = 'start date'
            self.filtered_data.loc[((self.filtered_data['YEAR4'] == curr_date.year) & (self.filtered_data['MONTH'] == curr_date.month) & (self.filtered_data['DAY'] < curr_date.day)), 'reason'] = 'start date'

        if selected_end_date is not None:
            curr_date = datetime.strptime(selected_end_date.strip(), '%Y-%m-%d')
            self.filtered_data.loc[self.filtered_data['YEAR4'] > curr_date.year, 'show'] = False
            self.filtered_data.loc[((self.filtered_data['YEAR4'] == curr_date.year) & (self.filtered_data['MONTH'] > curr_date.month)), 'show'] = False
            self.filtered_data.loc[((self.filtered_data['YEAR4'] == curr_date.year) & (self.filtered_data['MONTH'] == curr_date.month) & (self.filtered_data['DAY'] > curr_date.day)), 'show'] = False
            
            self.filtered_data.loc[self.filtered_data['YEAR4'] > curr_date.year, 'reason'] = 'end date'
            self.filtered_data.loc[((self.filtered_data['YEAR4'] == curr_date.year) & (self.filtered_data['MONTH'] > curr_date.month)), 'reason'] = 'end date'
            self.filtered_data.loc[((self.filtered_data['YEAR4'] == curr_date.year) & (self.filtered_data['MONTH'] == curr_date.month) & (self.filtered_data['DAY'] > curr_date.day)), 'reason'] = 'end date'

        if selected_time is not None:
            start_time = selected_time[0]
            end_time = selected_time[1]
            self.filtered_data.loc[self.filtered_data['time'] < start_time, 'show'] = False
            self.filtered_data.loc[self.filtered_data['time'] > end_time, 'show'] = False
            
            self.filtered_data.loc[self.filtered_data['time'] < start_time, 'reason'] = 'start time'
            self.filtered_data.loc[self.filtered_data['time'] > end_time, 'reason'] = 'end time'

    def get_figure(self):
        curr_fig = px.scatter_mapbox(
            self.filtered_data,
            lat="Latitude",
            lon="Longitud",
            hover_name="reason",
            hover_data={'show': False, "CASKLDRR": True, "CASINJRR": True, "personel": True, "ENGRS": True, "FIREMEN": True, "CONDUCTR": True, "BRAKEMEN": True},
            custom_data=["ID"],
            color=self.filtered_data['show'],
            color_discrete_map={False: "gray", True: "red"},
            zoom=self.zoom,
            center=self.center,
        )

        curr_fig.update_layout(
            mapbox=dict(
                style="open-street-map",
                zoom=self.zoom,
                center=self.center,
                bounds={"west": -160, "east": -30, "south": 0, "north": 75},
            ),
            dragmode="select",
            uirevision=True,
        )
        curr_fig.update_traces(
            selected=dict(marker=dict(opacity=1.0)),
            unselected=dict(marker=dict(opacity=1.0))
        )
        curr_fig.update_layout(showlegend=False)
        curr_fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

        return curr_fig
    
    def update_view(self, obj):
        if obj is not None:
            if obj.get('map.center') is not None:
                self.center = obj.get('map.center')
            
            if obj.get('map.zoom') is not None:
                self.zoom = obj.get('map.zoom')

    def update(self, 
               selected_points,
               selected_state, 
               selected_weather, 
               selected_visibility, 
               selected_temperature,
               selected_train_track, 
               selected_acc_type,
               selected_train_speed,
               selected_tons,
               selected_equipment_damage,
               selected_track_damage,
               selected_reportable_damage,
               selected_people_killed,
               selected_people_injured,
               selected_personel_duty,
               selected_engineers_duty,
               selected_firemen_duty,
               selected_conductors_duty,
               selected_brakemen_duty,
               selected_start_date, 
               selected_end_date, 
               selected_time):
        self.filter_data(selected_points,
                         selected_state, 
                         selected_weather, 
                         selected_visibility, 
                         selected_temperature,
                         selected_train_track, 
                         selected_acc_type,
                         selected_train_speed,
                         selected_tons,
                         selected_equipment_damage,
                         selected_track_damage,
                         selected_reportable_damage,
                         selected_people_killed,
                         selected_people_injured,
                         selected_personel_duty,
                         selected_engineers_duty,
                         selected_firemen_duty,
                         selected_conductors_duty,
                         selected_brakemen_duty,
                         selected_start_date, 
                         selected_end_date, 
                         selected_time)

        self.fig = self.get_figure()

        return self.fig
