import tkinter as tk
import time
import datetime
import threading
import owmapi
import conversions
import matplotlib.pyplot as plt

class Display():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Weather Display")
        self.root.geometry("1280x1024")
        #                               OMW API_Key
        self.owmapi = owmapi.OMWAPI("OWM API KEY")

    def setup(self):
        """
        Setup the layout of the display
        """
        # Create widgets
        
        # Colors #050249 #050249


        # Color Frames
        color_frame1 = tk.Frame(bg="#050249",height=370,width=740)
        color_frame2 = tk.Frame(bg="#050249",height=330,width=548)
        color_frame3 = tk.Frame(bg="#050249",height=654,width=740)
        color_frame4 = tk.Frame(bg="#050249",height=584,width=548)
        color_frame5 = tk.Frame(bg="#050249",height=130,width=548)

        # Titles
        expprecip = tk.Label(self.root,text="Expected Precipitation (Next1h)",fg="white",bg="#050249",pady=10,height=1,font="Helvetica 20 bold")
        hourly_temps = tk.Label(self.root,text="Forecasted Temperatures",fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        hourly_pops = tk.Label(self.root,text="Forecasted Precipitation Chances",fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")


        # Time labels
        self.zulu_time = tk.Label(self.root,fg="white",bg="#050249",font="Helvetica 30 bold",pady=10,height=1)
        self.local_time = tk.Label(self.root,fg="white",bg="#050249",font="Helvetica 30 bold",pady=10,height=1)
        

        # Current Weather
        self.weather_icon = tk.Label(self.root,bg="#050249")
        self.description = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=2,font="Helvetica 25 bold",wraplength=500)
        self.temp = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.feels_like = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.pressure = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.humidity = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.wind = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.rain = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.snow = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.clouds = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.sunrise = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.uvi = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.dewpoint = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.visibility = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")

        # Minutely Data
        self.minutely_graph = tk.Label(self.root,bg="#050249")

        # Hourly Data
        self.hourly_temps_graph = tk.Label(self.root,bg="#050249")
        self.hourly_pops_graph = tk.Label(self.root, bg="#050249")

        self.houricon1 = tk.Label(self.root, bg="#050249")
        self.hourlabel1 = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")

        self.houricon2 = tk.Label(self.root, bg="#050249")
        self.hourlabel2 = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.houricon3 = tk.Label(self.root, bg="#050249")
        self.hourlabel3 = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.houricon4 = tk.Label(self.root, bg="#050249")
        self.hourlabel4 = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.houricon5 = tk.Label(self.root, bg="#050249")
        self.hourlabel5 = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.houricon6 = tk.Label(self.root, bg="#050249")
        self.hourlabel6 = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.houricon7 = tk.Label(self.root, bg="#050249")
        self.hourlabel7 = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.houricon8 = tk.Label(self.root, bg="#050249")
        self.hourlabel8 = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.houricon9 = tk.Label(self.root, bg="#050249")
        self.hourlabel9 = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.houricon10 = tk.Label(self.root, bg="#050249")
        self.hourlabel10 = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.houricon11 = tk.Label(self.root, bg="#050249")
        self.hourlabel11 = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.houricon12 = tk.Label(self.root, bg="#050249")
        self.hourlabel12 = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")

        # Daily Data
        self.dayicon1 = tk.Label(self.root, bg="#050249")
        self.daylabel1 = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.dayicon2 = tk.Label(self.root, bg="#050249")
        self.daylabel2 = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.dayicon3 = tk.Label(self.root, bg="#050249")
        self.daylabel3 = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.dayicon4 = tk.Label(self.root, bg="#050249")
        self.daylabel4 = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.dayicon5 = tk.Label(self.root, bg="#050249")
        self.daylabel5 = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.dayicon6 = tk.Label(self.root, bg="#050249")
        self.daylabel6 = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.dayicon7 = tk.Label(self.root, bg="#050249")
        self.daylabel7 = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")

        

        # Rotating hour data
        self.rothourlabel = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 20 bold")
        self.rothourtemp = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.rothourwind = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.rothourcloud = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.rothourhumidity = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.rothourpop = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")

        # Rotating day data
        self.rotdaylabel = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 20 bold")
        self.rotdaytemp = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.rotdaywind = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.rotdaycloud = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.rotdayhumidity = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.rotdaypop = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.rotdaysun = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.rotdayuv = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")
        self.rotdayrain = tk.Label(self.root,fg="white",bg="#050249",pady=10,height=1,font="Helvetica 15 bold")

        


        # Place widgets
        color_frame1.place(x=548,y=0)
        color_frame2.place(x=0,y=130)
        color_frame3.place(x=548,y=370)
        color_frame4.place(x=0,y=450)
        color_frame5.place(x=0,y=0)
        expprecip.place(x=30,y=140)
        hourly_temps.place(x=600, y=380)
        hourly_pops.place(x=900,y=380)
        self.houricon1.place(x=580,y=680)
        self.hourlabel1.place(x=680,y=710)
        self.houricon2.place(x=580,y=760)
        self.hourlabel2.place(x=680,y=790)
        self.houricon3.place(x=580,y=840)
        self.hourlabel3.place(x=680,y=870)
        self.houricon4.place(x=580,y=920)
        self.hourlabel4.place(x=680,y=950)
        self.houricon5.place(x=750,y=680)
        self.hourlabel5.place(x=850,y=710)
        self.houricon6.place(x=750,y=760)
        self.hourlabel6.place(x=850,y=790)
        self.houricon7.place(x=750,y=840)
        self.hourlabel7.place(x=850,y=870)
        self.houricon8.place(x=750,y=920)
        self.hourlabel8.place(x=850,y=950)
        self.houricon9.place(x=920,y=680)
        self.hourlabel9.place(x=1020,y=710)
        self.houricon10.place(x=920,y=760)
        self.hourlabel10.place(x=1020,y=790)
        self.houricon11.place(x=920,y=840)
        self.hourlabel11.place(x=1020,y=870)
        self.houricon12.place(x=920,y=920)
        self.hourlabel12.place(x=1020,y=950)

        self.rotdaylabel.place(x=370,y=470)
        self.rotdaytemp.place(x=310,y=540)
        self.rotdaywind.place(x=310,y=590)
        self.rotdaycloud.place(x=310,y=640)
        self.rotdayhumidity.place(x=310,y=690)
        self.rotdaypop.place(x=310,y=740)
        self.rotdaysun.place(x=310,y=790)
        self.rotdayuv.place(x=310,y=840)
        self.rotdayrain.place(x=310,y=890)
        
        self.dayicon1.place(x=10,y=450)
        self.daylabel1.place(x=110,y=480)
        self.dayicon2.place(x=10,y=530)
        self.daylabel2.place(x=110,y=560)
        self.dayicon3.place(x=10,y=610)
        self.daylabel3.place(x=110,y=640)
        self.dayicon4.place(x=10,y=690)
        self.daylabel4.place(x=110,y=720)
        self.dayicon5.place(x=10,y=770)
        self.daylabel5.place(x=110,y=800)
        self.dayicon6.place(x=10,y=850)
        self.daylabel6.place(x=110,y=880)
        self.dayicon7.place(x=10,y=930)
        self.daylabel7.place(x=110,y=960)

        self.rothourlabel.place(x=1150,y=710)
        self.rothourtemp.place(x=1110,y=760)
        self.rothourwind.place(x=1110,y=810)
        self.rothourcloud.place(x=1110,y=860)
        self.rothourhumidity.place(x=1110,y=910)
        self.rothourpop.place(x=1110,y=960)

        self.hourly_temps_graph.place(x=555,y=420)
        self.hourly_pops_graph.place(x=910,y=420)
        self.minutely_graph.place(x=100,y=180)

        self.description.place(x=750, y=0)
        self.weather_icon.place(x=600,y=0)
        self.temp.place(x=600,y=110)
        self.feels_like.place(x=810,y=110)
        self.humidity.place(x=1090, y=110)
        self.pressure.place(x=1020,y=210)
        self.wind.place(x=600, y=210)
        self.clouds.place(x=1120,y=160)
        self.rain.place(x=600,y=260)
        self.snow.place(x=850, y=260)
        self.uvi.place(x=1100,y=260)
        self.dewpoint.place(x=950,y=160)
        self.sunrise.place(x=600,y=160)
        self.visibility.place(x=600,y=310)

        self.zulu_time.place(x=55,y=0)
        self.local_time.place(x=55, y=60)

    def main(self):
        """
        Code to run in main thread
        """
        past_current_weather = None
        past_minutely = None
        past_hourly = None
        past_daily = None
        #Wait for initilization
        time.sleep(5)
        while True:

            #Set datetime fields
            currentutc_dt = datetime.datetime.utcnow()
            current_dt = datetime.datetime.now()     

            self.zulu_time.configure(text=" Zulu: " + self.format_time(currentutc_dt,colon=True)+ " " + self.format_date(currentutc_dt))
            self.local_time.configure(text="Local: " + self.format_time(current_dt,colon=True) + " " + self.format_date(current_dt))

            


            # Set current weather fields
            if self.current_weather != past_current_weather:
                past_current_weather = self.current_weather
                self.set_current_weather_fields()

                # Set Icon
                icon_image = tk.PhotoImage(file="icons/"+self.current_weather["weather"][0]["icon"]+".png")
                self.weather_icon.configure(image=icon_image)
            
            if self.minutely_data != past_minutely:
                past_minutely = self.minutely_data
                if len(self.minutely_data) != 0:
                    times = []
                    volumes = []
                    currentunix = int(time.time())

                    # Get Data
                    for datapoint in self.minutely_data:
                        if datapoint["dt"] < currentunix:
                            continue
                        times.append(int((datapoint["dt"]-currentunix)/60))
                        volumes.append(conversions.Length.mmtoin(datapoint["precipitation"]))

                    # Create and save graph
                
                    # Create new figure
                    fig = plt.figure()

                    # Add graph and set data
                    ax = fig.add_subplot(111)
                    ax.plot(times, volumes,color="#00E0FF")
                    ax.set_xlabel("Minutes from " + self.format_time(current_dt,colon=True))
                    ax.set_ylabel("Expected Percipitation (in.)")
                    if max(volumes) == 0:
                        ax.set_yticks([0])


                    # Format graph and change colors
                    ax.spines['bottom'].set_color('white')
                    ax.spines['top'].set_color('white')
                    ax.spines['left'].set_color('white')
                    ax.spines['right'].set_color('white')
                    ax.xaxis.label.set_color('white')
                    ax.yaxis.label.set_color('white')
                    ax.tick_params(axis='x', colors='white')
                    ax.tick_params(axis='y', colors='white')

                    # Export to png
                    fig.savefig("graphs/expprecip.png",dpi=55,transparent=True)

                    # Set image to display
                    minutely_graph_image = tk.PhotoImage(file="graphs/expprecip.png")
                    self.minutely_graph.configure(image=minutely_graph_image)
            
            if self.hourly_data != past_hourly:
                past_hourly = self.hourly_data
                times = []
                self.datas = []
                temps = []
                pops = []
                ticks = []
                currentunix = int(time.time())

                # Get Hourly data
                for data in self.hourly_data:
                    if data["dt"] < currentunix:
                        continue
                    hour_delta = round((data["dt"]-currentunix)/3600)

                    # Only get next 16 hours
                    if hour_delta > 16:
                        break
                    
                    # Create display ticks list for plot
                    if hour_delta%2 == 0:
                        ticks.append(self.format_time(datetime.datetime.fromtimestamp(data["dt"]),colon=True))
                    self.datas.append(data)
                    times.append(self.format_time(datetime.datetime.fromtimestamp(data["dt"]),colon=True))
                    temps.append(conversions.Temperature.ktof(data["temp"]))
                    pops.append(data["pop"]*100)
                

                # Set data in lists
                hicon_image1 = tk.PhotoImage(file="icons/"+self.datas[0]["weather"][0]["icon"]+".png")
                self.houricon1.configure(image=hicon_image1)
                self.hourlabel1.configure(text=times[0])
                hicon_image2 = tk.PhotoImage(file="icons/"+self.datas[1]["weather"][0]["icon"]+".png")
                self.houricon2.configure(image=hicon_image2)
                self.hourlabel2.configure(text=times[1])
                hicon_image3 = tk.PhotoImage(file="icons/"+self.datas[2]["weather"][0]["icon"]+".png")
                self.houricon3.configure(image=hicon_image3)
                self.hourlabel3.configure(text=times[2])
                hicon_image4 = tk.PhotoImage(file="icons/"+self.datas[3]["weather"][0]["icon"]+".png")
                self.houricon4.configure(image=hicon_image4)
                self.hourlabel4.configure(text=times[3])
                hicon_image5 = tk.PhotoImage(file="icons/"+self.datas[4]["weather"][0]["icon"]+".png")
                self.houricon5.configure(image=hicon_image5)
                self.hourlabel5.configure(text=times[4])
                hicon_image6 = tk.PhotoImage(file="icons/"+self.datas[5]["weather"][0]["icon"]+".png")
                self.houricon6.configure(image=hicon_image6)
                self.hourlabel6.configure(text=times[5])
                hicon_image7 = tk.PhotoImage(file="icons/"+self.datas[6]["weather"][0]["icon"]+".png")
                self.houricon7.configure(image=hicon_image7)
                self.hourlabel7.configure(text=times[6])
                hicon_image8 = tk.PhotoImage(file="icons/"+self.datas[7]["weather"][0]["icon"]+".png")
                self.houricon8.configure(image=hicon_image8)
                self.hourlabel8.configure(text=times[7])
                hicon_image9 = tk.PhotoImage(file="icons/"+self.datas[8]["weather"][0]["icon"]+".png")
                self.houricon9.configure(image=hicon_image9)
                self.hourlabel9.configure(text=times[8])
                hicon_image10 = tk.PhotoImage(file="icons/"+self.datas[9]["weather"][0]["icon"]+".png")
                self.houricon10.configure(image=hicon_image10)
                self.hourlabel10.configure(text=times[9])
                hicon_image11 = tk.PhotoImage(file="icons/"+self.datas[10]["weather"][0]["icon"]+".png")
                self.houricon11.configure(image=hicon_image11)
                self.hourlabel11.configure(text=times[10])
                hicon_image12 = tk.PhotoImage(file="icons/"+self.datas[11]["weather"][0]["icon"]+".png")
                self.houricon12.configure(image=hicon_image12)
                self.hourlabel12.configure(text=times[11])




                # Create temperatures plot
                fig = plt.figure()

                # Add graph and set data
                ax = fig.add_subplot(111)
                ax.plot(times, temps, color="#FF5A00",markevery=2)
                ax.set_xlabel("Times")
                ax.set_ylabel("Temperatures (°F)")
                ax.set_xticks(ticks)

                # Format graph and change colors
                ax.spines['bottom'].set_color('white')
                ax.spines['top'].set_color('white')
                ax.spines['left'].set_color('white')
                ax.spines['right'].set_color('white')
                ax.xaxis.label.set_color('white')
                ax.yaxis.label.set_color('white')
                ax.tick_params(axis='x', colors='white')
                ax.tick_params(axis='y', colors='white')

                fig.savefig("graphs/hourlytemps.png",dpi=55,transparent=True)

                # Set image to display
                hourly_graph_image = tk.PhotoImage(file="graphs/hourlytemps.png")
                self.hourly_temps_graph.configure(image=hourly_graph_image)

                # Pops plot
                fig = plt.figure()

                # Add graph and set data
                ax = fig.add_subplot(111)
                ax.plot(times, pops, color="#00E0FF",markevery=2)
                ax.set_xlabel("Times")
                ax.set_ylabel("Probability of Precipitation(%)")
                if max(pops) == 0:
                    ax.set_yticks([0])
                ax.set_xticks(ticks)
                

                # Format graph and change colors
                ax.spines['bottom'].set_color('white')
                ax.spines['top'].set_color('white')
                ax.spines['left'].set_color('white')
                ax.spines['right'].set_color('white')
                ax.xaxis.label.set_color('white')
                ax.yaxis.label.set_color('white')
                ax.tick_params(axis='x', colors='white')
                ax.tick_params(axis='y', colors='white')

                # Export to png
                fig.savefig("graphs/hourlypops.png",dpi=55,transparent=True)

                # Set image to display
                hourly_pops_image = tk.PhotoImage(file="graphs/hourlypops.png")
                self.hourly_pops_graph.configure(image=hourly_pops_image)
            

             # Wait 1 second till repeating
            
            if self.daily_data != past_daily:
                past_daily = self.daily_data

                dicon_image1 = tk.PhotoImage(file="icons/"+self.daily_data[1]["weather"][0]["icon"]+".png")
                self.dayicon1.configure(image=dicon_image1)
                self.daylabel1.configure(text=self.format_date(datetime.datetime.fromtimestamp(self.daily_data[1]["dt"])) + " " + str(conversions.Temperature.ktof(self.daily_data[1]["temp"]["max"])) + "°F " + str(int(self.daily_data[1]["pop"]*100))+"%")
                dicon_image2 = tk.PhotoImage(file="icons/"+self.daily_data[2]["weather"][0]["icon"]+".png")
                self.dayicon2.configure(image=dicon_image2)
                self.daylabel2.configure(text=self.format_date(datetime.datetime.fromtimestamp(self.daily_data[2]["dt"])) + " " + str(conversions.Temperature.ktof(self.daily_data[2]["temp"]["max"])) + "°F " + str(int(self.daily_data[2]["pop"]*100))+"%")
                dicon_image3 = tk.PhotoImage(file="icons/"+self.daily_data[3]["weather"][0]["icon"]+".png")
                self.dayicon3.configure(image=dicon_image3)
                self.daylabel3.configure(text=self.format_date(datetime.datetime.fromtimestamp(self.daily_data[3]["dt"])) + " " + str(conversions.Temperature.ktof(self.daily_data[3]["temp"]["max"])) + "°F " + str(int(self.daily_data[3]["pop"]*100))+"%")
                dicon_image4 = tk.PhotoImage(file="icons/"+self.daily_data[4]["weather"][0]["icon"]+".png")
                self.dayicon4.configure(image=dicon_image4)
                self.daylabel4.configure(text=self.format_date(datetime.datetime.fromtimestamp(self.daily_data[4]["dt"])) + " " + str(conversions.Temperature.ktof(self.daily_data[4]["temp"]["max"])) + "°F " + str(int(self.daily_data[4]["pop"]*100))+"%")
                dicon_image5 = tk.PhotoImage(file="icons/"+self.daily_data[5]["weather"][0]["icon"]+".png")
                self.dayicon5.configure(image=dicon_image5)
                self.daylabel5.configure(text=self.format_date(datetime.datetime.fromtimestamp(self.daily_data[5]["dt"])) + " " + str(conversions.Temperature.ktof(self.daily_data[5]["temp"]["max"])) + "°F " + str(int(self.daily_data[5]["pop"]*100))+"%")
                dicon_image6 = tk.PhotoImage(file="icons/"+self.daily_data[6]["weather"][0]["icon"]+".png")
                self.dayicon6.configure(image=dicon_image6)
                self.daylabel6.configure(text=self.format_date(datetime.datetime.fromtimestamp(self.daily_data[6]["dt"])) + " " + str(conversions.Temperature.ktof(self.daily_data[6]["temp"]["max"])) + "°F " + str(int(self.daily_data[6]["pop"]*100))+"%")
                dicon_image7 = tk.PhotoImage(file="icons/"+self.daily_data[7]["weather"][0]["icon"]+".png")
                self.dayicon7.configure(image=dicon_image7)
                self.daylabel7.configure(text=self.format_date(datetime.datetime.fromtimestamp(self.daily_data[7]["dt"])) + " " + str(conversions.Temperature.ktof(self.daily_data[7]["temp"]["max"])) + "°F " + str(int(self.daily_data[7]["pop"]*100))+"%")
            
            time.sleep(1)


    def set_current_weather_fields(self):

        # Set Description
        self.description.configure(text=self.current_weather["weather"][0]["description"])

        # Set Temp
        raw_temp = self.current_weather["temp"]
        self.temp.configure(text="Temp: " +str(conversions.Temperature.ktof(raw_temp))+ "°F/" + str(conversions.Temperature.ktoc(raw_temp))+ "°C")

        # Set Feels like
        raw_temp = self.current_weather["feels_like"]
        self.feels_like.configure(text="Feels Like: " +str(conversions.Temperature.ktof(raw_temp))+ "°F/" + str(conversions.Temperature.ktoc(raw_temp))+ "°C")

        # Set Pressure

        self.pressure.configure(text="Pressure: " + str(conversions.Pressure.hpatoinhg(self.current_weather["pressure"]))+ " inHg")

        # Set Humidity

        self.humidity.configure(text="Humidity: " + str(self.current_weather["humidity"]) +"%")

        # Set Wind
        if "wind_gust" in self.current_weather.keys():
            self.wind.configure(text="Wind: "+str(conversions.Speed.mpstomph(self.current_weather["wind_speed"]))+"mph/"+str(conversions.Speed.mpstomph(self.current_weather["wind_speed"]))+"kt @ "+str(self.current_weather["wind_deg"])+"° G: "+str(conversions.Speed.mpstomph(self.current_weather["wind_gust"]))+"MPH/"+str(conversions.Speed.mpstoknot(self.current_weather["wind_gust"]))+"kt")
        else:
            self.wind.configure(text="Wind: "+str(conversions.Speed.mpstomph(self.current_weather["wind_speed"]))+"mph/"+str(conversions.Speed.mpstomph(self.current_weather["wind_speed"]))+"kt @ "+str(self.current_weather["wind_deg"])+"°")

        # Set Cloudiness
        self.clouds.configure(text="Clouds: "+str(self.current_weather["clouds"])+"%")

        # Set Uv index
        self.uvi.configure(text="UVI: "+str(round(self.current_weather["uvi"], 1))+"/10")

        # Set Dewpoint

        self.dewpoint.configure(text="DP: "+str(conversions.Temperature.ktof(self.current_weather["dew_point"]))+ "°F/" + str(conversions.Temperature.ktoc(self.current_weather["dew_point"]))+ "°C")

        # Set Rain

        if "rain" in self.current_weather.keys():
            rain_data = self.current_weather["rain"]
            self.rain.configure(text="Rain(Past1h): "+str(conversions.Length.mmtoin(rain_data["1h"]))+"in/"+str(rain_data["1h"])+"mm")
        else:
            self.rain.configure(text="Rain(Past1h): None")

        # Set Snow

        if "snow" in self.current_weather.keys():
            snow_data = self.current_weather["snow"]
            self.snow.configure(text="Snow(Past1h): "+str(conversions.Length.mmtoin(snow_data["1h"]))+"in/"+str(snow_data["1h"])+"mm")
        else:
            self.snow.configure(text="Snow(Past1h): None")

        # Set Sunrise and Sunset
        sunrise_time = datetime.datetime.fromtimestamp(self.current_weather["sunrise"])
        sunset_time = datetime.datetime.fromtimestamp(self.current_weather["sunset"])
        self.sunrise.configure(text="Sunrise/Sunset: "+self.format_time(sunrise_time, colon=True)+"/"+self.format_time(sunset_time, colon=True))

        # Set Visibility

        self.visibility.configure(text="Visibility: " +str(conversions.Length.mtosm(self.current_weather["visibility"])) + "SM")

            
    
    def weather_loop(self):
        """
        Code to get weather information
        """
        while True:
            onecall_data = self.owmapi.make_request("https://api.openweathermap.org/data/2.5/onecall?lat=INSERT_LATITUDE&lon=INSERT_LONGITUDE")
            self.current_weather = onecall_data["current"]
            if "minutely" in onecall_data.keys():
                self.minutely_data = onecall_data["minutely"]
            else:
                self.minutely_data = []
            self.hourly_data = onecall_data["hourly"]
            self.daily_data = onecall_data["daily"]
            time.sleep(600)
    
    def rotate_loop(self):
        """
        Rotates the rotating displays
        """
        time.sleep(5)
        
        while True:
            currentunix = int(time.time())
            for data in self.hourly_data:
                if data["dt"] < currentunix:
                        continue
                hour_delta = round((data["dt"]-currentunix)/3600)

                # Only get next 16 hours
                if hour_delta > 16:
                    break
                self.rothourlabel.configure(text=self.format_time(datetime.datetime.fromtimestamp(data["dt"]),colon=True))
                self.rothourtemp.configure(text="T: "+str(conversions.Temperature.ktof(data["temp"])) + "°F/" + str(conversions.Temperature.ktoc(data["temp"]))+"°C")
                self.rothourwind.configure(text="W: "+str(conversions.Speed.mpstomph(data["wind_speed"]))+"mph@"+str(data["wind_deg"])+"°")
                self.rothourcloud.configure(text="C: "+str(data["clouds"])+"%")
                self.rothourhumidity.configure(text="H: "+str(data["humidity"])+"%")
                self.rothourpop.configure(text="POP: "+str(int(data["pop"]*100))+"%")
                time.sleep(5)
    
    def day_rotate_loop(self):
        time.sleep(5)
        while True:
            for i in range(8):
                if i == 0:
                    continue
                self.rotdaylabel.configure(text=self.format_date(datetime.datetime.fromtimestamp(self.daily_data[i]["dt"])))
                self.rotdaytemp.configure(text="T: "+str(conversions.Temperature.ktof(self.daily_data[i]["temp"]["max"])) + "°F/" + str(conversions.Temperature.ktoc(self.daily_data[i]["temp"]["max"]))+"°C")
                self.rotdaywind.configure(text="W: "+str(conversions.Speed.mpstomph(self.daily_data[i]["wind_speed"]))+"mph@"+str(self.daily_data[i]["wind_deg"])+"°")
                self.rotdaycloud.configure(text="C: "+str(self.daily_data[i]["clouds"])+"%")
                self.rotdayhumidity.configure(text="H: "+str(self.daily_data[i]["humidity"])+"%")
                self.rotdaypop.configure(text="POP: "+str(int(self.daily_data[i]["pop"]*100))+"%")
                self.rotdaysun.configure(text="S: " + self.format_time(datetime.datetime.fromtimestamp(self.daily_data[i]["sunrise"]),colon=True) + "/" + self.format_time(datetime.datetime.fromtimestamp(self.daily_data[i]["sunset"]),colon=True))
                if "uvi" in self.daily_data[i].keys():
                    uvi_data = self.daily_data[i]["uvi"]
                else:
                    uvi_data = "None"
                self.rotdayuv.configure(text="UVI: " + str(uvi_data) + "/10")
                if "rain" in self.daily_data[i].keys():
                    rain_data = str(conversions.Length.mmtoin(self.daily_data[i]["rain"])) + " in."
                else:
                    rain_data = "None"

                self.rotdayrain.configure(text="R: " + rain_data)
                time.sleep(10)
                    
    
    def format_date(self,datetime):
        """
        Helper function to format months and days of a datetime
        """
        if datetime.month < 10:
            months = "0" + str(datetime.month)
        else:
            months = datetime.month
        
        if datetime.day < 10:
            days = "0" + str(datetime.day)
        else:
            days = datetime.day

        return str(months) + "/" + str(days)
    
    def format_time(self, datetime, colon=False):
        """
        Helper function to format hour and minutes of a datetime
        """
        if datetime.hour < 10:
            hours = "0" + str(datetime.hour)
        else:
            hours = datetime.hour
        
        if datetime.minute < 10:
            minutes = "0" + str(datetime.minute)
        else:
            minutes = datetime.minute
        
        if colon:
            return str(hours) + ":"+str(minutes)
        return str(hours)+str(minutes)


if __name__ == "__main__":
    UI = Display()
    

    UI.setup()

    # Start weather thread
    threading.Thread(target=UI.weather_loop,daemon=True).start()

    # Start main thread
    threading.Thread(target=UI.main,daemon=True).start()

    # Start rotating thread
    threading.Thread(target=UI.rotate_loop,daemon=True).start()

    # Start day rotating threadd
    threading.Thread(target=UI.day_rotate_loop,daemon=True).start()

    UI.root.mainloop()





