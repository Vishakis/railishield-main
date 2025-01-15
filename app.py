from jbi100_app.config import state_options, state_name, state_code
from jbi100_app.main import app
from jbi100_app.views.menu import make_menu_layout
from jbi100_app.views.scatterplot import Scatterplot
from jbi100_app.views.mapplot import Mapplot
from jbi100_app.views.barchart import Barchart
from jbi100_app.views.linechart import Linechart
from jbi100_app.data import get_data

from dash import html, ctx, dcc
from dash.exceptions import PreventUpdate
import plotly.express as px
from dash.dependencies import Input, Output


if __name__ == '__main__':
    # Create data
    data = get_data()


    # Instantiate custom views
    curr_mapplot = Mapplot("Mapplot 1", data)
    curr_plot_1 = Linechart('Plot 1', data, 'TYPE', 'TEMP', 'Type of accident', 'Temperature')
    curr_plot_2 = Barchart('Plot 2', data, 'TEMP', 'Temperature')

    app.layout = html.Div(
        id="app-container",
        children=[
            # Left column
            html.Div(
                id="left-column",
                className="three columns",
                children=make_menu_layout()
            ),

            # Right column
            html.Div(
                id="right-column",
                className="nine columns",
                children=[
                    curr_mapplot,
                    html.Div(
                        id="plot-row",
                        className="nine columns",
                        children=[
                            curr_plot_1,
                            curr_plot_2
                        ], style={'width': '49%', 'display': 'flex', 'flex-direction': 'row'},
                    ),
                ],
            ),


        ],
    )
    
    # Define interactions
    @app.callback(
        Output('hidden-div', "value"), [
        Input(curr_mapplot.html_id, "relayoutData"),
    ])
    def update_mapplot(data):
        curr_mapplot.update_view(data)
        return None

    @app.callback(
        Output(curr_mapplot.html_id, "figure"), [
        Input(curr_mapplot.html_id, "selectedData"),
        Input("select-state", "value"),
        Input("select-weather", "value"),
        Input("select-visibility", "value"),
        Input('select-temperature', 'value'),
        Input("select-track-type", "value"),
        Input("select-acc-type", "value"),
        Input('select-train-speed', 'value'),
        Input('select-tons', 'value'),
        Input('select-equipment-damage', 'value'),
        Input('select-track-damage', 'value'),
        Input('select-reportable-damage', 'value'),
        Input('select-people-killed', 'value'),
        Input('select-people-injured', 'value'),
        Input('select-personel-duty', 'value'),
        Input('select-engineers-duty', 'value'),
        Input('select-firemen-duty', 'value'),
        Input('select-conductors-duty', 'value'),
        Input('select-brakemen-duty', 'value'),
        Input('select-date', 'start_date'),
        Input('select-date', 'end_date'),
        Input('select-time', 'value'),
    ])
    def update_mapplot(selected_points,
                       selected_state, 
                       selected_weather, 
                       selected_visibility, 
                       selected_temperature,
                       selected_track_type, 
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
        return curr_mapplot.update(selected_points,
                                   selected_state, 
                                   selected_weather, 
                                   selected_visibility, 
                                   selected_temperature,
                                   selected_track_type, 
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
    
    @app.callback(
        Output(curr_plot_1.html_id, "figure"), [
        Input(curr_mapplot.html_id, "selectedData"),
        Input("select-state", "value"),
        Input("select-weather", "value"),
        Input("select-visibility", "value"),
        Input('select-temperature', 'value'),
        Input("select-track-type", "value"),
        Input("select-acc-type", "value"),
        Input('select-train-speed', 'value'),
        Input('select-tons', 'value'),
        Input('select-equipment-damage', 'value'),
        Input('select-track-damage', 'value'),
        Input('select-reportable-damage', 'value'),
        Input('select-people-killed', 'value'),
        Input('select-people-injured', 'value'),
        Input('select-personel-duty', 'value'),
        Input('select-engineers-duty', 'value'),
        Input('select-firemen-duty', 'value'),
        Input('select-conductors-duty', 'value'),
        Input('select-brakemen-duty', 'value'),
        Input('select-date', 'start_date'),
        Input('select-date', 'end_date'),
        Input('select-time', 'value'),
        Input('select-left-plot', 'value'),
        Input('select-left-plot-mean', 'value'),
    ])
    def update_plot_1(selected_points,
                      selected_state, 
                      selected_weather, 
                      selected_visibility, 
                      selected_temperature,
                      selected_track_type, 
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
        return curr_plot_1.update(selected_points,
                                  selected_state, 
                                  selected_weather, 
                                  selected_visibility, 
                                  selected_temperature,
                                  selected_track_type, 
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
                                  selected_plot_mean)
    
    @app.callback(
        Output(curr_plot_2.html_id, "figure"), [
        Input(curr_mapplot.html_id, "selectedData"),
        Input("select-state", "value"),
        Input("select-weather", "value"),
        Input("select-visibility", "value"),
        Input('select-temperature', 'value'),
        Input("select-track-type", "value"),
        Input("select-acc-type", "value"),
        Input('select-train-speed', 'value'),
        Input('select-tons', 'value'),
        Input('select-equipment-damage', 'value'),
        Input('select-track-damage', 'value'),
        Input('select-reportable-damage', 'value'),
        Input('select-people-killed', 'value'),
        Input('select-people-injured', 'value'),
        Input('select-personel-duty', 'value'),
        Input('select-engineers-duty', 'value'),
        Input('select-firemen-duty', 'value'),
        Input('select-conductors-duty', 'value'),
        Input('select-brakemen-duty', 'value'),
        Input('select-date', 'start_date'),
        Input('select-date', 'end_date'),
        Input('select-time', 'value'),
        Input('select-right-plot', 'value'),
    ])
    def update_plot_2(selected_points,
                      selected_state, 
                      selected_weather, 
                      selected_visibility, 
                      selected_temperature,
                      selected_track_type, 
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
        return curr_plot_2.update(selected_points,
                                  selected_state, 
                                  selected_weather, 
                                  selected_visibility, 
                                  selected_temperature,
                                  selected_track_type, 
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
                                  selected_plot)


    # Tooltip for Temperature Slider
    @app.callback(
        Output('tooltip-temperature', 'children'),
        Input('select-temperature', 'value')
    )
    def update_temperature_tooltip(value):
        if value:
            return f"Temperature range °F: {value[0]} - {value[1]}"
        return ""

    #Tooltip for Time range slider
    @app.callback(
        Output('tooltip-time', 'children'),  # Update the tooltip's content
        [Input('select-time', 'value')]  # Listen to changes in the time range slider
    )
    def update_time_tooltip(value):
        if value:

            start_time, end_time = value


            def round_half_up(value):
                return int(value + 0.5)  # Adds 0.5 and truncates to simulate "round half up" behavior


            start_time = round_half_up(start_time)
            end_time = round_half_up(end_time)


            return f"Time Range: {start_time}:00 - {end_time}:00"

        return "Time Range: Not selected"


    # Tooltip for Speed of Train Slider
    @app.callback(
        Output('tooltip-train-speed', 'children'),
        Input('select-train-speed', 'value')
    )
    def update_train_speed_tooltip(value):
        if value:
            return f"Speed range m/h: {value[0]} - {value[1]}"
        return ""


    # Tooltip for Trailing Tons Slider
    @app.callback(
        Output('tooltip-tons', 'children'),
        Input('select-tons', 'value')
    )
    def update_tons_tooltip(value):
        if value:
            return f"Weight range: {value[0]} - {value[1]}"
        return ""

    # Define reset button interactions
    @app.callback(
        Output(curr_mapplot.html_id, 'selectedData'),
        Input('reset-filters', 'n_clicks'),
        prevent_initial_call=True
    )
    def update_selected(n_clicks):
        return None
    
    @app.callback(
        Output('select-state', 'value'),
        Input('reset-filters', 'n_clicks'),
        prevent_initial_call=True
    )
    def update_state(n_clicks):
        return None
    
    @app.callback(
        Output('select-weather', 'value'),
        [Input('reset-filters', 'n_clicks'),
        Input(curr_plot_1.html_id, "clickData"),
        Input(curr_plot_2.html_id, "clickData"),],
        prevent_initial_call=True
    )
    def update_weather(n_clicks, click_plot_1, click_plot_2):
        item_clicked = ctx.triggered_id
        
        if click_plot_1 is not None and item_clicked == curr_plot_1.html_id:
            curr_output = curr_plot_1.update_filter(click_plot_1, 'WEATHER')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
        
        if click_plot_2 is not None and item_clicked == curr_plot_2.html_id:
            curr_output = curr_plot_2.update_filter(click_plot_2, 'WEATHER')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate

        return None
    
    @app.callback(
        Output('select-visibility', 'value'),
        [Input('reset-filters', 'n_clicks'),
        Input(curr_plot_1.html_id, "clickData"),
        Input(curr_plot_2.html_id, "clickData"),],
        prevent_initial_call=True
    )
    def update_visibility(n_clicks, click_plot_1, click_plot_2):
        item_clicked = ctx.triggered_id
        
        if click_plot_1 is not None and item_clicked == curr_plot_1.html_id:
            curr_output = curr_plot_1.update_filter(click_plot_1, 'VISIBILITY')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
        
        if click_plot_2 is not None and item_clicked == curr_plot_2.html_id:
            curr_output = curr_plot_2.update_filter(click_plot_2, 'VISIBILITY')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate

        return None
    
    @app.callback(
        Output('select-temperature', 'value'),
        [Input('reset-filters', 'n_clicks'),
        Input(curr_plot_1.html_id, "clickData"),
        Input(curr_plot_2.html_id, "clickData"),],
        prevent_initial_call=True
    )
    def update_temperature(n_clicks, click_plot_1, click_plot_2):
        item_clicked = ctx.triggered_id
        
        if click_plot_1 is not None and item_clicked == curr_plot_1.html_id:
            curr_output = curr_plot_1.update_filter(click_plot_1, 'TEMP')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
        
        if click_plot_2 is not None and item_clicked == curr_plot_2.html_id:
            curr_output = curr_plot_2.update_filter(click_plot_2, 'TEMP')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
            
        return [-65, 862]
        
    @app.callback(
        Output('select-track-type', 'value'),
        [Input('reset-filters', 'n_clicks'),
        Input(curr_plot_1.html_id, "clickData"),
        Input(curr_plot_2.html_id, "clickData"),],
        prevent_initial_call=True
    )
    def update_track_type(n_clicks, click_plot_1, click_plot_2):
        item_clicked = ctx.triggered_id
        
        if click_plot_1 is not None and item_clicked == curr_plot_1.html_id:
            curr_output = curr_plot_1.update_filter(click_plot_1, 'TYPTRK')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
        
        if click_plot_2 is not None and item_clicked == curr_plot_2.html_id:
            curr_output = curr_plot_2.update_filter(click_plot_2, 'TYPTRK')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate

        return None

    @app.callback(
        Output('select-acc-type', 'value'),
        [Input('reset-filters', 'n_clicks'),
        Input(curr_plot_1.html_id, "clickData"),
        Input(curr_plot_2.html_id, "clickData"),],
        prevent_initial_call=True
    )
    def update_acc_type(n_clicks, click_plot_1, click_plot_2):
        item_clicked = ctx.triggered_id
        
        if click_plot_1 is not None and item_clicked == curr_plot_1.html_id:
            curr_output = curr_plot_1.update_filter(click_plot_1, 'TYPE')
            print('click data: ', click_plot_1)
            print('output: ', curr_output)
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
        
        if click_plot_2 is not None and item_clicked == curr_plot_2.html_id:
            curr_output = curr_plot_2.update_filter(click_plot_2, 'TYPE')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate

        return None
    
    @app.callback(
        Output('select-train-speed', 'value'),
        [Input('reset-filters', 'n_clicks'),
        Input(curr_plot_1.html_id, "clickData"),
        Input(curr_plot_2.html_id, "clickData"),],
        prevent_initial_call=True
    )
    def update_train_speed(n_clicks, click_plot_1, click_plot_2):
        item_clicked = ctx.triggered_id
        
        if click_plot_1 is not None and item_clicked == curr_plot_1.html_id:
            curr_output = curr_plot_1.update_filter(click_plot_1, 'TRNSPD')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
        
        if click_plot_2 is not None and item_clicked == curr_plot_2.html_id:
            curr_output = curr_plot_2.update_filter(click_plot_2, 'TRNSPD')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
            
        return [0, 150]
    
    @app.callback(
        Output('select-tons', 'value'),
        [Input('reset-filters', 'n_clicks'),
        Input(curr_plot_1.html_id, "clickData"),
        Input(curr_plot_2.html_id, "clickData"),],
        prevent_initial_call=True
    )
    def update_train_speed(n_clicks, click_plot_1, click_plot_2):
        item_clicked = ctx.triggered_id
        
        if click_plot_1 is not None and item_clicked == curr_plot_1.html_id:
            curr_output = curr_plot_1.update_filter(click_plot_1, 'TONS')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
        
        if click_plot_2 is not None and item_clicked == curr_plot_2.html_id:
            curr_output = curr_plot_2.update_filter(click_plot_2, 'TONS')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
            
        return [0, 99000]
    
    @app.callback(
        Output('select-equipment-damage', 'value'),
        [Input('reset-filters', 'n_clicks'),
        Input(curr_plot_1.html_id, "clickData"),
        Input(curr_plot_2.html_id, "clickData"),],
        prevent_initial_call=True
    )
    def update_train_speed(n_clicks, click_plot_1, click_plot_2):
        item_clicked = ctx.triggered_id
        
        if click_plot_1 is not None and item_clicked == curr_plot_1.html_id:
            curr_output = curr_plot_1.update_filter(click_plot_1, 'EQPDMG')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
        
        if click_plot_2 is not None and item_clicked == curr_plot_2.html_id:
            curr_output = curr_plot_2.update_filter(click_plot_2, 'EQPDMG')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
            
        return [0, 27140000]
    
    @app.callback(
        Output('select-track-damage', 'value'),
        [Input('reset-filters', 'n_clicks'),
        Input(curr_plot_1.html_id, "clickData"),
        Input(curr_plot_2.html_id, "clickData"),],
        prevent_initial_call=True
    )
    def update_train_speed(n_clicks, click_plot_1, click_plot_2):
        item_clicked = ctx.triggered_id
        
        if click_plot_1 is not None and item_clicked == curr_plot_1.html_id:
            curr_output = curr_plot_1.update_filter(click_plot_1, 'TRKDMG')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
        
        if click_plot_2 is not None and item_clicked == curr_plot_2.html_id:
            curr_output = curr_plot_2.update_filter(click_plot_2, 'TRKDMG')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
            
        return [0, 10400000]
    
    @app.callback(
        Output('select-reportable-damage', 'value'),
        [Input('reset-filters', 'n_clicks'),
        Input(curr_plot_1.html_id, "clickData"),
        Input(curr_plot_2.html_id, "clickData"),],
        prevent_initial_call=True
    )
    def update_train_speed(n_clicks, click_plot_1, click_plot_2):
        item_clicked = ctx.triggered_id
        
        if click_plot_1 is not None and item_clicked == curr_plot_1.html_id:
            curr_output = curr_plot_1.update_filter(click_plot_1, 'ACCDMG')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
        
        if click_plot_2 is not None and item_clicked == curr_plot_2.html_id:
            curr_output = curr_plot_2.update_filter(click_plot_2, 'ACCDMG')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
            
        return [0, 31538754]
    
    @app.callback(
        Output('select-people-killed', 'value'),
        [Input('reset-filters', 'n_clicks'),
        Input(curr_plot_1.html_id, "clickData"),
        Input(curr_plot_2.html_id, "clickData"),],
        prevent_initial_call=True
    )
    def update_weather(n_clicks, click_plot_1, click_plot_2):
        item_clicked = ctx.triggered_id
        
        if click_plot_1 is not None and item_clicked == curr_plot_1.html_id:
            curr_output = curr_plot_1.update_filter(click_plot_1, 'CASKLDRR')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
        
        if click_plot_2 is not None and item_clicked == curr_plot_2.html_id:
            curr_output = curr_plot_2.update_filter(click_plot_2, 'CASKLDRR')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate

        return None
    
    @app.callback(
        Output('select-people-injured', 'value'),
        [Input('reset-filters', 'n_clicks'),
        Input(curr_plot_1.html_id, "clickData"),
        Input(curr_plot_2.html_id, "clickData"),],
        prevent_initial_call=True
    )
    def update_weather(n_clicks, click_plot_1, click_plot_2):
        item_clicked = ctx.triggered_id
        
        if click_plot_1 is not None and item_clicked == curr_plot_1.html_id:
            curr_output = curr_plot_1.update_filter(click_plot_1, 'CASINJRR')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
        
        if click_plot_2 is not None and item_clicked == curr_plot_2.html_id:
            curr_output = curr_plot_2.update_filter(click_plot_2, 'CASINJRR')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate

        return None
    
    @app.callback(
        Output('select-personel-duty', 'value'),
        [Input('reset-filters', 'n_clicks'),
        Input(curr_plot_1.html_id, "clickData"),
        Input(curr_plot_2.html_id, "clickData"),],
        prevent_initial_call=True
    )
    def update_weather(n_clicks, click_plot_1, click_plot_2):
        item_clicked = ctx.triggered_id
        
        if click_plot_1 is not None and item_clicked == curr_plot_1.html_id:
            curr_output = curr_plot_1.update_filter(click_plot_1, 'personel')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
        
        if click_plot_2 is not None and item_clicked == curr_plot_2.html_id:
            curr_output = curr_plot_2.update_filter(click_plot_2, 'personel')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate

        return None
    
    @app.callback(
        Output('select-engineers-duty', 'value'),
        [Input('reset-filters', 'n_clicks'),
        Input(curr_plot_1.html_id, "clickData"),
        Input(curr_plot_2.html_id, "clickData"),],
        prevent_initial_call=True
    )
    def update_weather(n_clicks, click_plot_1, click_plot_2):
        item_clicked = ctx.triggered_id
        
        if click_plot_1 is not None and item_clicked == curr_plot_1.html_id:
            curr_output = curr_plot_1.update_filter(click_plot_1, 'ENGRS')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
        
        if click_plot_2 is not None and item_clicked == curr_plot_2.html_id:
            curr_output = curr_plot_2.update_filter(click_plot_2, 'ENGRS')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate

        return None
    
    @app.callback(
        Output('select-firemen-duty', 'value'),
        [Input('reset-filters', 'n_clicks'),
        Input(curr_plot_1.html_id, "clickData"),
        Input(curr_plot_2.html_id, "clickData"),],
        prevent_initial_call=True
    )
    def update_weather(n_clicks, click_plot_1, click_plot_2):
        item_clicked = ctx.triggered_id
        
        if click_plot_1 is not None and item_clicked == curr_plot_1.html_id:
            curr_output = curr_plot_1.update_filter(click_plot_1, 'FIREMEN')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
        
        if click_plot_2 is not None and item_clicked == curr_plot_2.html_id:
            curr_output = curr_plot_2.update_filter(click_plot_2, 'FIREMEN')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate

        return None
    
    @app.callback(
        Output('select-conductors-duty', 'value'),
        [Input('reset-filters', 'n_clicks'),
        Input(curr_plot_1.html_id, "clickData"),
        Input(curr_plot_2.html_id, "clickData"),],
        prevent_initial_call=True
    )
    def update_weather(n_clicks, click_plot_1, click_plot_2):
        item_clicked = ctx.triggered_id
        
        if click_plot_1 is not None and item_clicked == curr_plot_1.html_id:
            curr_output = curr_plot_1.update_filter(click_plot_1, 'CONDUCTR')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
        
        if click_plot_2 is not None and item_clicked == curr_plot_2.html_id:
            curr_output = curr_plot_2.update_filter(click_plot_2, 'CONDUCTR')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate

        return None
    
    @app.callback(
        Output('select-brakemen-duty', 'value'),
        [Input('reset-filters', 'n_clicks'),
        Input(curr_plot_1.html_id, "clickData"),
        Input(curr_plot_2.html_id, "clickData"),],
        prevent_initial_call=True
    )
    def update_weather(n_clicks, click_plot_1, click_plot_2):
        item_clicked = ctx.triggered_id
        
        if click_plot_1 is not None and item_clicked == curr_plot_1.html_id:
            curr_output = curr_plot_1.update_filter(click_plot_1, 'BRAKEMEN')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate
        
        if click_plot_2 is not None and item_clicked == curr_plot_2.html_id:
            curr_output = curr_plot_2.update_filter(click_plot_2, 'BRAKEMEN')
            if curr_output is not None:
                return curr_output
            else:
                raise PreventUpdate

        return None
    
    @app.callback(
        Output('select-date', 'start_date'),
        Input('reset-filters', 'n_clicks'),
        prevent_initial_call=True
    )
    def update_start_date(n_clicks):
        return '2002-01-01'
    
    @app.callback(
        Output('select-date', 'end_date'),
        Input('reset-filters', 'n_clicks'),
        prevent_initial_call=True
    )
    def update_end_date(n_clicks):
        return '2024-12-31'
    
    @app.callback(
        Output('select-time', 'value'),
        Input('reset-filters', 'n_clicks'),
        prevent_initial_call=True
    )
    def update_time(n_clicks):
        return [0, 24]

    app.run_server(debug=False, dev_tools_ui=False)