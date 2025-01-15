from dash import dcc, html
import plotly.express as px

import pandas as pd
from datetime import datetime
import math

from ..config import visibility_to_code, weather_to_code, type_track_to_code, acc_type_to_code
from ..config import visibility_mapping, weather_mapping, type_track_mapping, acc_type_mapping
from ..config import type_to_label

from ..general import split_number_dash


class Barchart(html.Div):
    def __init__(self, name, df, type, title):
        self.html_id = name.lower().replace(" ", "-")
        self.loading_id = 'loading-' + name.lower().replace(" ", "-")
        self.df = df
        self.type = type
        self.title = title
        self.bar_limit = 3
        self.num_buckets = 5
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

    def get_bar_chart_data(self, data, col_name, bar_lim, mapping=None):
        curr_value_counts =  data[col_name].value_counts()
        df_curr = pd.DataFrame(data={'value': curr_value_counts.index, 'count': curr_value_counts.tolist()})
        df_curr.sort_values('count', ascending=False, inplace=True)

        total_rest_sum = df_curr.loc[bar_lim:, 'count'].sum()

        df_curr = df_curr[:bar_lim]

        if mapping is not None:
            df_curr[['value']] = df_curr[['value']].replace(mapping.set_index('code')['text'])
        else:
            df_curr['value'] = df_curr['value'].astype(int).astype(str)

        df_curr.loc[len(df_curr)] = {'value': 'Other', 'count': total_rest_sum}

        return df_curr
    
    def get_range_data(self, data, col_name, num_buckets):
        curr_min = data[col_name].min()
        curr_max = data[col_name].max()

        curr_bucket_size = math.ceil((curr_max - curr_min)/num_buckets)

        curr_value = []
        curr_count = []

        for i in range(0, num_buckets):
            curr_start = curr_min + i*curr_bucket_size
            curr_end = curr_min + i*curr_bucket_size + curr_bucket_size
            
            curr_value.append(str(curr_start) + '-' + str(curr_end))
            curr_count.append(data.loc[((data[col_name] >= curr_start) & (data[col_name] < curr_end)), col_name].count())

        return pd.DataFrame({'value': curr_value, 'count': curr_count})

    def get_figure(self):
        curr_fig = None

        if self.type == 'TYPE':
            curr_data = self.get_bar_chart_data(self.filtered_data, self.type, self.bar_limit, acc_type_mapping)

            curr_fig = px.bar(curr_data, 
                              x='value', 
                              y='count',
                              labels={'value':'Accident type', 'count': 'Number of accidents'},
                              title=self.title)


        if self.type == 'TEMP':
            curr_data = self.get_range_data(self.filtered_data, self.type, self.num_buckets)

            curr_fig = px.bar(curr_data, 
                              x='value', 
                              y='count',
                              labels={'value':'Temperature range', 'count': 'Number of accidents'},
                              title=self.title)

        if self.type == 'VISIBLTY':
            curr_data = self.get_bar_chart_data(self.filtered_data, self.type, self.bar_limit, visibility_mapping)

            curr_fig = px.bar(curr_data, 
                              x='value', 
                              y='count',
                              labels={'value':'Visibility', 'count': 'Number of accidents'},
                              title=self.title)

        if self.type == 'WEATHER':
            curr_data = self.get_bar_chart_data(self.filtered_data, self.type, self.bar_limit, weather_mapping)

            curr_fig = px.bar(curr_data, 
                              x='value', 
                              y='count',
                              labels={'value':'Weather', 'count': 'Number of accidents'},
                              title=self.title)

        if self.type == 'TRNSPD':
            curr_data = self.get_range_data(self.filtered_data, self.type, self.num_buckets)

            curr_fig = px.bar(curr_data, 
                              x='value', 
                              y='count',
                              labels={'value':'Train speed range', 'count': 'Number of accidents'},
                              title=self.title)

        if self.type == 'TONS':
            curr_data = self.get_range_data(self.filtered_data, self.type, self.num_buckets)

            curr_fig = px.bar(curr_data, 
                              x='value', 
                              y='count',
                              labels={'value':'Weight range (tons)', 'count': 'Number of accidents'},
                              title=self.title)

        if self.type == 'TYPTRK':
            curr_data = self.get_bar_chart_data(self.filtered_data, self.type, self.bar_limit, type_track_mapping)

            curr_fig = px.bar(curr_data, 
                              x='value', 
                              y='count',
                              labels={'value':'Track type', 'count': 'Number of accidents'},
                              title=self.title)

        if self.type == 'EQPDMG':
            curr_data = self.get_range_data(self.filtered_data, self.type, self.num_buckets)

            curr_fig = px.bar(curr_data, 
                              x='value', 
                              y='count',
                              labels={'value':'equipment damage range', 'count': 'number of accidents'},
                              title=self.title)

        if self.type == 'TRKDMG':
            curr_data = self.get_range_data(self.filtered_data, self.type, self.num_buckets)

            curr_fig = px.bar(curr_data, 
                              x='value', 
                              y='count',
                              labels={'value':'track damage range', 'count': 'number of accidents'},
                              title=self.title)

        if self.type == 'CASKLDRR':
            curr_data = self.get_bar_chart_data(self.filtered_data, self.type, self.bar_limit)

            curr_fig = px.bar(curr_data, 
                              x='value', 
                              y='count',
                              labels={'value':'number of people killed', 'count': 'number of accidents'},
                              title=self.title)

        if self.type == 'CASINJRR':
            curr_data = self.get_bar_chart_data(self.filtered_data, self.type, self.bar_limit)

            curr_fig = px.bar(curr_data, 
                              x='value', 
                              y='count',
                              labels={'value':'number of people injured', 'count': 'number of accidents'},
                              title=self.title)

        if self.type == 'ACCDMG':
            curr_data = self.get_range_data(self.filtered_data, self.type, self.num_buckets)

            curr_fig = px.bar(curr_data, 
                              x='value', 
                              y='count',
                              labels={'value':'accident damage range', 'count': 'number of accidents'},
                              title=self.title)

        if self.type == 'personel':
            curr_data = self.get_bar_chart_data(self.filtered_data, self.type, self.bar_limit)

            curr_fig = px.bar(curr_data, 
                              x='value', 
                              y='count',
                              labels={'value':'personel on duty', 'count': 'number of accidents'},
                              title=self.title)

        if self.type == 'ENGRS':
            curr_data = self.get_bar_chart_data(self.filtered_data, self.type, self.bar_limit)

            curr_fig = px.bar(curr_data, 
                              x='value', 
                              y='count',
                              labels={'value':'engineers on duty', 'count': 'number of accidents'},
                              title=self.title)

        if self.type == 'FIREMEN':
            curr_data = self.get_bar_chart_data(self.filtered_data, self.type, self.bar_limit)

            curr_fig = px.bar(curr_data, 
                              x='value', 
                              y='count',
                              labels={'value':'firemen on duty', 'count': 'number of accidents'},
                              title=self.title)

        if self.type == 'CONDUCTR':
            curr_data = self.get_bar_chart_data(self.filtered_data, self.type, self.bar_limit)

            curr_fig = px.bar(curr_data, 
                              x='value', 
                              y='count',
                              labels={'value':'conductors on duty', 'count': 'number of accidents'},
                              title=self.title)

        if self.type == 'BRAKEMEN':
            curr_data = self.get_bar_chart_data(self.filtered_data, self.type, self.bar_limit)

            curr_fig = px.bar(curr_data, 
                              x='value', 
                              y='count',
                              labels={'value':'brakemen on duty', 'count': 'number of accidents'},
                              title=self.title)
            
        curr_fig.update_traces(customdata=[self.type]*len(curr_fig.data[0].x))
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
               selected_plot):
        self.type = selected_plot
        self.title = type_to_label.get(self.type)

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
        curr_plot_type = click_plot['points'][0]['customdata']
        curr_plot_label = click_plot['points'][0]['label']
        if curr_plot_type == type and curr_plot_label != 'Other':
            return split_number_dash(curr_plot_label)
        else:
            return None
