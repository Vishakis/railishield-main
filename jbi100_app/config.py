# Here you can add any global configuations
import pandas as pd
from datetime import date

def create_mapping(dictionary):
    df_curr = pd.DataFrame.from_dict(dictionary, columns=['code'], orient='index')
    df_curr['text'] = df_curr.index
    df_curr.reset_index(drop=True, inplace=True)

    return df_curr

color_list1 = ["green", "blue"]
color_list2 = ["red", "purple"]


visibility_list = ['Dawn', 'Day', 'Dusk', 'Dark']
weather_list = ['Clear', 'Cloudy', 'Rain', 'Fog', 'Sleet', 'Snow']
type_track_list = ['Main', 'Yard', 'Siding', 'Industry']
acc_type_list = ['Derailment', ' Head on collision', ' Rear end collision', 'Side Collision',
                 'Raking collision', 'Broken train collision', 'Hay-rail crossing', 'RR grade crossing', 
                 'Obstruction', ' Explosion-detonation', 'Fire/violent rupture', 'Other impacts', 'Other']

visibility_to_code = {'Dawn': 1.0, 'Day': 2.0, 'Dusk': 3.0, 'Dark': 4.0}
weather_to_code = {'Clear': 1.0, 'Cloudy': 2.0, 'Rain': 3.0, 'Fog': 4.0, 'Sleet': 5.0, 'Snow': 6.0}
type_track_to_code = {'Main': 1, 'Yard': 2, 'Siding': 3, 'Industry': 4}
acc_type_to_code = {'Derailment': 1., ' Head on collision': 2., ' Rear end collision': 3., 'Side Collision': 4.,
                 'Raking collision': 5., 'Broken train collision': 6., 'Hay-rail crossing': 7., 'RR grade crossing': 8., 
                 'Obstruction': 9., ' Explosion-detonation': 10., 'Fire/violent rupture': 11., 'Other impacts': 12., 
                 'Other': 13.}

visibility_mapping = create_mapping(visibility_to_code)
weather_mapping = create_mapping(weather_to_code)
type_track_mapping = create_mapping(type_track_to_code)
acc_type_mapping = create_mapping(acc_type_to_code)

type_to_label = {'TYPE': 'Type of accident',
                 'TEMP': 'Temperature',
                 'VISIBLTY': 'Visibility',
                 'WEATHER': 'Weather',
                 'TRNSPD': 'Speed of train',
                 'TONS': 'Trailing tons',
                 'TYPTRK': 'Type of track',
                 'EQPDMG': 'Damage to equipment',
                 'TRKDMG': 'Damage to the track',}
                 # 'CASKLDRR': 'People killed',
                 # 'CASINJRR': 'People injured',
                 # 'ACCDMG': 'Reportable damage',
                 # 'personel': 'Personel on duty',
                 # 'ENGRS': 'Engineers on duty',
                 # 'FIREMEN': 'Firemen on duty',
                 # 'CONDUCTR': 'Conductors on duty',
                 # 'BRAKEMEN': 'Brakemen on duty',}

type_to_label_descrete = {'TYPE': 'Type of accident',
                          'VISIBLTY': 'Visibility',
                          'WEATHER': 'Weather',
                          'TYPTRK': 'Type of track',}
                          # 'personel': 'Personel on duty',
                          # 'ENGRS': 'Engineers on duty',
                          # 'FIREMEN': 'Firemen on duty',
                          # 'CONDUCTR': 'Conductors on duty',
                          # 'BRAKEMEN': 'Brakemen on duty',}

type_to_label_continious = {'TEMP': 'Temperature',
                            'TRNSPD': 'Speed of train',
                            'TONS': 'Trailing tons',
                            'EQPDMG': 'Damage to equipment',
                            'TRKDMG': 'Damage to the track',}
                            # 'CASKLDRR': 'People killed',
                            # 'CASINJRR': 'People injured',
                            # 'ACCDMG': 'Reportable damage',
                            # 'personel': 'Personel on duty',
                            # 'ENGRS': 'Engineers on duty',
                            # 'FIREMEN': 'Firemen on duty',
                            # 'CONDUCTR': 'Conductors on duty',
                            # 'BRAKEMEN': 'Brakemen on duty',}

plot_options = [{'label': j, 'value': i} for i, j in type_to_label.items()]
plot_options_descrete = [{'label': j, 'value': i} for i, j in type_to_label_descrete.items()]
plot_options_continious = [{'label': j, 'value': i} for i, j in type_to_label_continious.items()]

state_code = [1, 2, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54, 55, 56]
state_name = ["ALABAMA", "ALASKA", "ARIZONA", "ARKANSAS", "CALIFORNIA", "COLORADO", "CONNECTICUT", "DELAWARE", "DISTRICT OF COLUMBIA", "FLORIDA", "GEORGIA", "HAWAII", "IDAHO", "ILLINOIS", "INDIANA", "IOWA", "KANSAS", "KENTUCKY", "LOUISIANA", "MAINE", "MARYLAND", "MASSACHUSETTS", "MICHIGAN", "MINNESOTA", "MISSISSIPPI", "MISSOURI", "MONTANA", "NEBRASKA", "NEVADA", "NEW HAMPSHIRE", "NEW JERSEY", "NEW MEXICO", "NEW YORK", "NORTH CAROLINA", "NORTH DAKOTA", "OHIO", "OKLAHOMA", "OREGON", "PENNSYLVANIA", "RHODE ISLAND", "SOUTH CAROLINA", "SOUTH DAKOTA", "TENNESSEE", "TEXAS", "UTAH", "VERMONT", "VIRGINIA", "WASHINGTON", "WEST VIRGINIA", "WISCONSIN", "WYOMING"]
state_name = [text.capitalize() for text in state_name]

state_options = [{'label': state_name[i], 'value': state_code[i]} for i in range(0, len(state_code))]

menu_default_values = {
    "STATE": None,
    "WEATHER": None,
    "VISIBLTY": None,
    "TEMP": [-65, 862],
    "TYPTRK": None,
    "TYPE": None,
    "TRNSPD": [0, 150],
    "TONS": [0, 99000],
    "EQPDMG": [0, 27140000],
    "TRKDMG": [0, 10400000],
    "ACCDMG": [0, 31538754],
    "CASKLDRR": None,
    "CASINJRR": None,
    "personel": None,
    "ENGRS": None,
    "FIREMEN": None,
    "CONDUCTR": None,
    "BRAKEMEN": None,
    "date_start": date(2002, 1, 1),
    "date_end": date(2024, 12, 31),
    "time": [0, 24],
}