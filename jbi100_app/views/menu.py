from dash import dcc, html

from ..config import visibility_list, weather_list, type_track_list, acc_type_list
from ..config import plot_options, plot_options_descrete, plot_options_continious, state_options
from ..config import menu_default_values


def generate_description_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card",
        children=[
            html.H5("RailShield"),
        ],
    )


def generate_control_card():
    """

    :return: A Div containing controls for graphs.
    """
    return html.Div(
        id="control-card",
        children=(
            # The hidden-div is used to do callbacks without an output (e.g., update mapplot.zoom)
            html.Div(id='hidden-div', style={'display': 'none'}),
            html.Button('Reset filters', id='reset-filters'),

            html.Div(
                id="select-date-wrapper",
                children=[
                    html.Label("Date"),
                    dcc.DatePickerRange(
                        id='select-date',
                        start_date=menu_default_values['date_start'],
                        end_date=menu_default_values['date_end'],
                        min_date_allowed=menu_default_values['date_start'],
                        max_date_allowed=menu_default_values['date_end'],
                    ),
                ]
            ),
            #html.Br(),
            html.Div(
                id="select-time-wrapper",
                children=[
                    html.Label("Time"),
                    html.Div(
                        id='tooltip-time',
                        children='Time Range:',  # The initial text (static)
                        style={'textAlign': 'center', 'fontSize': '12px', 'color': 'black'}
                    ),
                    dcc.RangeSlider(
                        menu_default_values['time'][0],  # Minimum value of slider
                        menu_default_values['time'][1],  # Maximum value of slider
                        value=menu_default_values['time'],  # Initial slider values
                        id='select-time'  # ID for callbacks
                    ),
                ],
                style={
                    "textAlign": "center",
                    "margin-bottom": "2px",
                    "display": "flex",
                    "flex-direction": "column",
                    "align-items": "center",
                },
            ),
            #html.Br(),
            html.Div(
                id="state-track-row",
                children=[
                    html.Div(
                        children=[
                            html.Label("State"),
                            dcc.Dropdown(
                                id="select-state",
                                options=state_options,
                                style={"width": "90%"},  # Optional inline style to control width
                            ),
                        ],
                        style={"flex": "1", "margin-right": "10px"}  # Adjust margin for spacing
                    ),
                    html.Div(
                        children=[
                            html.Label("Track type"),
                            dcc.Dropdown(
                                id="select-track-type",
                                options=[{"label": i, "value": i} for i in type_track_list],
                                style={"width": "90%"},  # Optional inline style to control width
                                searchable=False
                            ),
                        ],
                        style={"flex": "1", "margin-left": "10px"}  # Adjust margin for spacing
                    ),
                ],
                style={"display": "flex", "justify-content": "space-between", "margin-bottom": "10px"}
            ),
            #html.Br(),
            html.Div(
                id="weather-visibility-row",
                children=[
                    html.Div(
                        children=[
                            html.Label("Weather"),
                            dcc.Dropdown(
                                id="select-weather",
                                options=[{"label": i, "value": i} for i in weather_list],
                                style={"width": "90%"},  # Optional inline style for width
                                searchable=False  # Disable search bar if not needed
                            ),
                        ],
                        style={"flex": "1", "margin-right": "10px"}  # Adjust margin for spacing
                    ),
                    html.Div(
                        children=[
                            html.Label("Visibility"),
                            dcc.Dropdown(
                                id="select-visibility",
                                options=[{"label": i, "value": i} for i in visibility_list],
                                style={"width": "90%"},  # Optional inline style for width
                                searchable=False  # Disable search bar if not needed
                            ),
                        ],
                        style={"flex": "1", "margin-left": "10px"}  # Adjust margin for spacing
                    ),
                ],
                style={"display": "flex", "justify-content": "space-between", "margin-bottom": "10px"}
                # Aligns row and spaces elements
            ),
            #html.Br(),
            html.Div(
                children=[
                    html.Label("Accident type"),
                    dcc.Dropdown(
                        id="select-acc-type",
                        options=[{"label": i, "value": i} for i in acc_type_list]
                    ),
                ],
                style={"textAlign": "center", "margin-bottom": "10px",
                       "width": "200px",  # Adjust width to make the container wider
                       "margin-inline": "auto",  # Center the container horizontally
                       },
            ),
            # html.Br()
            html.Div(
                id="select-temperature-wrapper",
                children=[
                    html.Label("Temperature"),
                    html.Div(id='tooltip-temperature',
                             style={'textAlign': 'center', 'fontSize': '12px', 'color': 'black'}
                             ),
                    dcc.RangeSlider(
                        menu_default_values['TEMP'][0],
                        menu_default_values['TEMP'][1],
                        value=menu_default_values['TEMP'],
                        id='select-temperature'
                    ),
                ],
                style={
                    "textAlign": "center",  # Center the label, tooltip, and slider
                    "margin-bottom": "2px",  # Add spacing between components
                    "display": "flex",
                    "flex-direction": "column",  # Stack label > tooltip > slider
                    "align-items": "center",
                },
            ),
            # html.Br()
            html.Div(
                id="select-train-speed-wrapper",
                children=[
                    html.Label("Speed of train"),
                    html.Div(id='tooltip-train-speed',
                             style={'textAlign': 'center', 'fontSize': '12px', 'color': 'black'}
                             ),
                    dcc.RangeSlider(
                        menu_default_values['TRNSPD'][0],
                        menu_default_values['TRNSPD'][1],
                        value=menu_default_values['TRNSPD'],
                        id='select-train-speed'
                    ),
                ],
                style={
                    "textAlign": "center",  # Center the label, tooltip, and slider
                    "margin-bottom": "2px",  # Add spacing between components
                    "display": "flex",
                    "flex-direction": "column",  # Stack label > tooltip > slider
                    "align-items": "center",
                },
            ),

            #html.Br()
            html.Div(
                id="select-tons-wrapper",
                children=[
                    html.Label("Trailing tons"),
                    html.Div(id='tooltip-tons',
                             style={'textAlign': 'center', 'fontSize': '12px', 'color': 'black'}
                             ),
                    dcc.RangeSlider(
                        menu_default_values['TONS'][0],
                        menu_default_values['TONS'][1],
                        value=menu_default_values['TONS'],
                        id='select-tons'
                    ),
                ],
                style={
                    "textAlign": "center",  # Center the label, tooltip, and slider
                    "margin-bottom": "2px",  # Add spacing between components
                    "display": "flex",
                    "flex-direction": "column",  # Stack label > tooltip > slider
                    "align-items": "center",
                },
            ),

            #html.Br(),
            html.Div(
                id="line-chart-mean-row",
                children=[
                    html.Div(
                        children=[
                            html.Label("Line Chart"),
                            dcc.Dropdown(
                                id="select-left-plot",
                                options=plot_options_descrete,
                                value='TYPE',
                                clearable=False,
                            ),
                        ],
                        style={"flex": "1", "margin-right": "10px"}  # Adjust spacing for alignment
                    ),
                    html.Div(
                        children=[
                            html.Label("Line Chart Mean"),
                            dcc.Dropdown(
                                id="select-left-plot-mean",
                                options=plot_options_continious,
                                value='TEMP',
                                clearable=False,
                            ),
                        ],
                        style={"flex": "1", "margin-left": "10px"}  # Adjust spacing for alignment
                    ),
                ],
                style={
                    "display": "flex",
                    "justify-content": "space-between",
                    "margin-bottom": "10px",  # Same style as Weather and Visibility row
                },
            ),

            html.Div(
                id="bar-chart-container",
                children=[
                    html.Label("Bar Chart"),
                    dcc.Dropdown(
                        id="select-right-plot",
                        options=plot_options,
                        value='TEMP',
                        clearable=False,
                    ),
                ],
                style={
                    "textAlign": "center",  # Center-align the label and dropdown
                    "margin-bottom": "10px",  # Add spacing below the dropdown
                    "width": "200px",  # Set a container width consistent with Accident Type Dropdown
                    "margin-inline": "auto",  # Center the dropdown container horizontally
                },
            ),

            html.Div(children=[
                html.Label("Damage to equipment"),
                dcc.RangeSlider(menu_default_values['EQPDMG'][0],
                                menu_default_values['EQPDMG'][1],
                                value=menu_default_values['EQPDMG'],
                                id='select-equipment-damage'),
                html.Br(),
                html.Label("Damage to track"),
                dcc.RangeSlider(menu_default_values['TRKDMG'][0],
                                menu_default_values['TRKDMG'][1],
                                value=menu_default_values['TRKDMG'],
                                id='select-track-damage'),
                html.Br(),
                html.Label("Reportable damage"),
                dcc.RangeSlider(menu_default_values['ACCDMG'][0],
                                menu_default_values['ACCDMG'][1],
                                value=menu_default_values['ACCDMG'],
                                id='select-reportable-damage'),
                html.Br(),
                html.Label("People killed"),
                dcc.Dropdown(
                    id="select-people-killed",
                    options=[{"label": str(i), "value": str(i)} for i in range(48)],
                ),
                html.Br(),
                html.Label("People injured"),
                dcc.Dropdown(
                    id="select-people-injured",
                    options=[{"label": str(i), "value": str(i)} for i in range(559)],
                ),
                html.Br(),
                html.Label("Personnel on duty"),
                dcc.Dropdown(
                    id="select-personel-duty",
                    options=[{"label": str(i), "value": str(i)} for i in range(10)],
                ),
                html.Br(),
                html.Label("Engineers on duty"),
                dcc.Dropdown(
                    id="select-engineers-duty",
                    options=[{"label": str(i), "value": str(i)} for i in range(10)],
                ),
                html.Br(),
                html.Label("Firemen on duty"),
                dcc.Dropdown(
                    id="select-firemen-duty",
                    options=[{"label": str(i), "value": str(i)} for i in range(10)],
                ),
                html.Br(),
                html.Label("Conductors on duty"),
                dcc.Dropdown(
                    id="select-conductors-duty",
                    options=[{"label": str(i), "value": str(i)} for i in range(10)],
                ),
                html.Br(),
                html.Label("Brakemen on duty"),
                dcc.Dropdown(
                    id="select-brakemen-duty",
                    options=[{"label": str(i), "value": str(i)} for i in range(10)],
                ),
            ], style='display:none'),
            #html.Br(),

            )
    )


def make_menu_layout():
    return [generate_description_card(), generate_control_card()]
