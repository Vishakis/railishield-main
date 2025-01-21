from dash import dcc, html
import plotly.express as px

import pandas as pd
from datetime import datetime
import math

from ..config import visibility_to_code, weather_to_code, type_track_to_code, acc_type_to_code
from ..config import visibility_mapping, weather_mapping, type_track_mapping, acc_type_mapping
from ..config import type_to_label

from ..general import split_number_dash


class Linechart(html.Div):
    def __init__(self, name, df, attr1, attr2, title1, title2):
        self.html_id = name.lower().replace(" ", "-")
        self.loading_id = 'loading-' + name.lower().replace(" ", "-")
        self.df = df
        self.attr1 = attr1
        self.attr2 = attr2
        self.title1 = title1
        self.title2 = title2
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
                    id=self.loading_id,
                    type="circle",
                    delay_show=0,
                    delay_hide=0,
                    children=dcc.Graph(id=self.html_id, figure=self.fig, config={"displayModeBar": False})
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
        self.filtered_data = self.df.copy()

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

        self.filtered_data = self.filtered_data[self.filtered_data['show'] == True]

    def get_line_chart_data(self, mapping=None):
        df_curr = self.filtered_data.copy()

        df_curr = df_curr[df_curr[self.attr1].notna()]
        df_curr = df_curr[df_curr['YEAR4'].notna()]

        if mapping is not None:
            df_curr[self.attr1] = df_curr[self.attr1].replace(mapping.set_index('code')['text'])
        else:
            df_curr[self.attr1] = df_curr[self.attr1].astype(int).astype(str)

        df_curr = df_curr.groupby([self.attr1, 'YEAR4'])[self.attr2].mean()

        # curr_index = df_curr.index.get_level_values(0).unique()

        df_curr = df_curr.reset_index()

        return df_curr

    def get_figure(self):
        curr_fig = None

        # Colorblind-friendly colors
        colorblind_colors = [
            '#377eb8',  # Blue
            '#ff7f00',  # Orange
            '#4daf4a',  # Green
            '#f781bf',  # Pink
            '#a65628',  # Brown
            '#984ea3',  # Purple
            '#999999',  # Gray
            '#e41a1c',  # Red
            '#dede00',  # Yellow
        ]

        if self.attr1 == 'TYPE':
            curr_mapping = acc_type_mapping
        elif self.attr1 == 'VISIBLTY':
            curr_mapping = visibility_mapping
        elif self.attr1 == 'WEATHER':
            curr_mapping = weather_mapping
        elif self.attr1 == 'TYPTRK':
            curr_mapping = type_track_mapping
        else:
            curr_mapping = None

        curr_data = self.get_line_chart_data(curr_mapping)

        # Set the colorblind colors as the default
        curr_fig = px.line(curr_data,
                           x="YEAR4",
                           y=self.attr2,
                           color=self.attr1,
                           markers=True,
                           custom_data=[curr_data[self.attr1], [self.attr1] * len(curr_data)],
                           color_discrete_sequence=colorblind_colors)  # Use the predefined color sequence
        curr_fig.update_traces(textposition="bottom right")
        curr_fig.update_layout(xaxis_title="Year",
                               yaxis_title=self.title2 + ' (mean)',
                               legend_title=self.title1, )

        return curr_fig

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
               selected_time,
               selected_plot,
               selected_plot_mean):
        self.attr1 = selected_plot
        self.title1 = type_to_label.get(self.attr1)
        self.attr2 = selected_plot_mean
        self.title2 = type_to_label.get(self.attr2)

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
    
    def update_filter(self, click_plot, type):
        # print('click plot: ', click_plot)
        # print('click type: ', type)
        if click_plot['points'][0].get('customdata') is None:
            return None
        curr_plot_type = click_plot['points'][0]['customdata'][1]
        curr_plot_label = click_plot['points'][0]['customdata'][0]
        if curr_plot_type == type and curr_plot_label != 'Other':
            return split_number_dash(curr_plot_label)
        else:
            return None
