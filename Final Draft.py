import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
from matplotlib import style
import matplotlib.animation as animation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

LARGE_FONT = ("Verdana",12)
style.use("ggplot")

df = pd.read_csv("final_merged_data.csv")
up_data = df[df['State'].str.contains("Uttar Pradesh")]
up_data = up_data.drop(['Non-Workers - PersonsLiterate'],axis = 1)
up_education = up_data[up_data.columns[:24]]
x1 = up_education["Non-Workers - FemalesGraduate and above other than Technical Degree"].item()
x2 = up_education["Non-Workers - FemalesIlliterate"].item()
x3 = up_education["Non-Workers - FemalesLiterate but below Matric/Secondary"].item()
x4 = up_education["Non-Workers - FemalesMatric/Secondary but below Graduate"].item()
x5 = up_education["Non-Workers - FemalesTechnical Degree or Diploma equal to Degree or Post-Graduate Degree"].item()
x6 = up_education["Non-Workers - FemalesTechnical Diploma or Certificate not equal to Degree"].item()
y1 = up_education["Non-Workers - MalesGraduate and above other than Technical Degree"].item()
y2 = up_education["Non-Workers - MalesIlliterate"].item()
y3 = up_education["Non-Workers - MalesLiterate but below Matric/Secondary"].item()
y4 = up_education["Non-Workers - MalesMatric/Secondary but below Graduate"].item()
y5 = up_education["Non-Workers - MalesTechnical Degree or Diploma equal to Degree or Post-Graduate Degree"].item()
y6 = up_education["Non-Workers - MalesTechnical Diploma or Certificate not equal to Degree"].item()
v1 = up_education["Non-Workers - PersonsGraduate and above other than Technical Degree"]/up_education["Non-Workers - PersonsTotal"]
v2 = up_education["Non-Workers - PersonsIlliterate"]/up_education["Non-Workers - PersonsTotal"]
v3 = up_education["Non-Workers - PersonsLiterate but below Matric/Secondary"]/up_education["Non-Workers - PersonsTotal"]
v4 = up_education["Non-Workers - PersonsMatric/Secondary but below Graduate"]/up_education["Non-Workers - PersonsTotal"]
v5 = up_education["Non-Workers - PersonsTechnical Degree or Diploma equal to Degree or Post-Graduate Degree"]/up_education["Non-Workers - PersonsTotal"]
v6 = up_education["Non-Workers - PersonsTechnical Diploma or Certificate not equal to Degree"]/up_education["Non-Workers - PersonsTotal"]
up_educ_data = {'Education category':['Graduate and above other than technical degree', 'Illiterate', 'Below matric/secondary',
                                              'Below Graduate','Degree/Post-Graduate degree','Diploma not degree'],
                       'Percentage':[v1.item(),v2.item(),v3.item(),v4.item(),v5.item(),v6.item()],
                       'Count for Females' :[x1,x2,x3,x4,x5,x6],
                       'Count for Males' :[y1,y2,y3,y4,y5,y6]}

up_educ_df = pd.DataFrame(up_educ_data)

class dab203app(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs) 
        tk.Tk.wm_title(self,"DAB 203 Project")
        container = tk.Frame(self)
        container.pack(side = "top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff = 0)
        filemenu.add_command(label="Exit",command = quit)
        menubar.add_cascade(label="Exit", menu=filemenu)
        tk.Tk.config(self, menu= menubar)        
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix, PageSeven, PageEight, PageNine, PageTen, PageEleven, PageTwelve, PageThirteen):
           frame = F(container,self)
           self.frames[F] = frame
           frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(StartPage)           
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
        
class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Welcome to our DAB 203 Project", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self,text = "Number of total non workers per Indian region", command = lambda : controller.show_frame(PageOne))
        button1.pack()
        button2 = ttk.Button(self,text = "Percentage of unemployed people by education category", command = lambda : controller.show_frame(PageTwo))
        button2.pack()
        button3 = ttk.Button(self,text = "Unemployed women count for different education categories", command = lambda : controller.show_frame(PageThree))
        button3.pack()
        button4 = ttk.Button(self,text = "Unemployed men count for different education categories", command = lambda : controller.show_frame(PageFour))
        button4.pack()
        button5 = ttk.Button(self,text = "Male and female suicide victim counts", command = lambda : controller.show_frame(PageFive))
        button5.pack()
        button6 = ttk.Button(self,text = "Region wise female suicide victims", command = lambda : controller.show_frame(PageSix))
        button6.pack()
        button7 = ttk.Button(self,text = "Suicide counts distribution by age group", command = lambda : controller.show_frame(PageSeven))
        button7.pack()
        button8 = ttk.Button(self,text = "Pensioners contributing to unemployment in India", command = lambda : controller.show_frame(PageEight))
        button8.pack()
        button9 = ttk.Button(self,text = "Dependents contributing to unemployment in India",
                           command = lambda : controller.show_frame(PageNine))
        button9.pack()
        button10 = ttk.Button(self,text = "People involved in household duties contributing to unemployment in India",
                           command = lambda : controller.show_frame(PageTen))
        button10.pack()
        button11 = ttk.Button(self,text = "Main Activity Beggars, Vagrants etc. - PersonsTotal",
                           command = lambda : controller.show_frame(PageEleven))
        button11.pack()
        button12 = ttk.Button(self,text = "Relationship between No. of literate non workers and No of people in 100 thousands who are below Poverty Line for all states",
                           command = lambda : controller.show_frame(PageTwelve))
        button12.pack()
        button13 = ttk.Button(self,text = "Relationship between No. of literate non workers and No of people in 100 thousands who are below Poverty Line for all states",
                           command = lambda : controller.show_frame(PageThirteen))
        button13.pack()

class PageOne(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Number of total non workers per Indian region", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button14 = ttk.Button(self,text = "Back To Home", command = lambda : controller.show_frame(StartPage))
        button14.pack()
        f =  Figure(figsize = (10,6), dpi = 60)
        a = f.add_subplot(111)
        a.set_title("Understanding the graph,it can be seen that the bar corresponding to Indian state Uttar Pradesh is the highest indicating that the state has worst unemployment situation.")
        x = df['State']
        y = df['Non-Workers - PersonsTotal']
        a.clear()
        a.bar(x,y,color='red')
        a.set_xlabel('State')
        a.set_ylabel('Non-Workers - PersonsTotal')
        a.tick_params(labelrotation=38)
        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class PageTwo(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Percentage of unemployed people by education category", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button15 = ttk.Button(self,text = "Back To Home", command = lambda : controller.show_frame(StartPage))
        button15.pack()
        f =  Figure(figsize = (10,6), dpi = 100)
        a = f.add_subplot(111)
        a.set_title("Quite visibly, majority of unemployed Uttar Pradesh residents are illiterate, the percentage is 46 to be precise.")
        labels = ['Graduate and above other than technical degree','Illiterate','Below matric/secondary','Below Graduate','','Diploma Not Degree']
        sizes = up_educ_df['Percentage']*2
        colors = ['yellowgreen','lightcoral','red','lightskyblue','pink','blue']
        explode = (0, 0, 0, 0, 0, 0)
        a.pie(sizes,explode = explode, labels = labels,colors = colors, autopct = '%1.1f%%',shadow = True, startangle = 180)
        a.axis('equal')
        a.legend(loc="lower left")
        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class PageThree(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Unemployed women count for different education categories", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button16 = ttk.Button(self,text = "Back To Home", command = lambda : controller.show_frame(StartPage))
        button16.pack()
        f =  Figure(figsize = (10,6), dpi = 100)
        a = f.add_subplot(111)
        a.set_title("Unemployment among women follow the overall trend noted in the visualization.")
        x = up_educ_df["Education category"]
        y = up_educ_df["Count for Females"]
        a.bar(x,y)
        a.set_xlabel('Education category')
        a.set_ylabel('Count for Females')
        a.tick_params(labelrotation=10)
        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class PageFour(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Unemployed men count for different education categories", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button17 = ttk.Button(self,text = "Back To Home", command = lambda : controller.show_frame(StartPage))
        button17.pack()
        f =  Figure(figsize = (5,5), dpi = 100)
        a = f.add_subplot(111)
        a.set_title("Surprisingly, literate men having qualification below matric or secondary are the most jobless among other education categories .")
        x = up_educ_df["Education category"]
        y = up_educ_df["Count for Males"]
        a.bar(x,y)
        a.set_xlabel('Education category')
        a.set_ylabel('Count for Males')
        a.tick_params(labelrotation=10)
        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class PageFive(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Male and female suicide victim counts", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button18 = ttk.Button(self,text = "Back To Home", command = lambda : controller.show_frame(StartPage))
        button18.pack()
        f =  Figure(figsize = (10,6), dpi = 100)
        a = f.add_subplot(111)
        a.set_title("Apparently, the suicide numbers seem to have a positive co-relation, Indian regions with less male suicide victims tend to have less female victims too and the other way around.")
        x = df['Total Male']
        y = df['Total Female']
        a.clear()
        a.scatter(x, y, color='green')
        a.set_xlabel('Total Males')
        a.set_ylabel('Total Females')
        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class PageSix(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Region wise female suicide victims", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button19 = ttk.Button(self,text = "Back To Home", command = lambda : controller.show_frame(StartPage))
        button19.pack()
        f =  Figure(figsize = (10,6), dpi = 60)
        a = f.add_subplot(111)
        a.set_title("Tamil Nadu and West Bengal had maximum number of female suicides")
        x = df["State"]
        y = df["Total Female"]
        a.bar(x, y)
        a.set_xlabel('State')
        a.set_ylabel('Total Females')
        a.tick_params(labelrotation=38)
        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class PageSeven(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Suicide percentage as per age of unemployed people", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button20 = ttk.Button(self,text = "Back To Home", command = lambda : controller.show_frame(StartPage))
        button20.pack()
        f =  Figure(figsize = (10,6), dpi = 100)
        a = f.add_subplot(111)
        a.set_title("Quite evidently, unemployed Indians aged 30-44 committed the greatest number of suicides.")
        upto_14_years = df["Male upto 14 years"].sum() + df["Female upto 14 years"].sum()
        between_15_29 = df["Male 15-29 years"].sum() + df["Female 15-29 years"].sum()
        between_30_44 = df["Male 30-44 years"].sum() + df["Female 30-44 years"].sum()
        between_45_59 = df["Male 45-59 years"].sum() + df["Female 45-59 years"].sum()
        above_60 = df["Male 60 years and above"].sum() + df["Female 60 years and above"].sum()
        Age_group = ['Upto 14 years', '15-29', '30-44','45-59', '60 and above']
        suicide_count = [upto_14_years,between_15_29,between_30_44,between_45_59 ,above_60]
        labels = Age_group
        colors = ['#FF0000', '#0000FF', '#FFFF00','#ADFF2F', '#FFA500']
        explode = (0.05, 0.05, 0.05, 0.05, 0.05)
        a.pie(suicide_count, colors=colors, labels=Age_group, autopct='%1.1f%%', pctdistance=0.85, explode=explode)
        a.legend(loc="lower left")
        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class PageEight(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Pensioners contributing to unemployment in India", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button21 = ttk.Button(self,text = "Back To Home", command = lambda : controller.show_frame(StartPage))
        button21.pack()
        f =  Figure(figsize = (10,6), dpi = 100)
        a = f.add_subplot(111)
        a.set_title("Number of people with Main activity as Pensioners are high in the state of Andhra Pradesh with above 1.75 million people.")
        x = df["State"]
        y = df["Main Activity Pensioners - PersonsTotal"]        
        a.set_title("Pensioners contributing to unemployment in India")        
        a.bar(x,y,color ='green')
        a.set_xlabel('State')
        a.set_ylabel('Main Activity Pensioners - PersonsTotal')
        a.tick_params(labelrotation=38)
        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class PageNine(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Dependents contributing to unemployment in India", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button22 = ttk.Button(self,text = "Back To Home", command = lambda : controller.show_frame(StartPage))
        button22.pack()
        f =  Figure(figsize = (10,6), dpi = 100)
        a = f.add_subplot(111)
        a.set_title("We can observe that the number of people with Main activity as Dependents are high in the state of Uttar Pradesh with just less than 40 million people.")
        x = df["State"]
        y = df["Main Activity Dependents - PersonsTotal"]        
        a.bar(x,y,color ='green')
        a.set_xlabel('State')
        a.set_ylabel('Main Activity Dependents - PersonsTotal')
        a.tick_params(labelrotation=38)
        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class PageTen(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="People involved in household duties contributing to unemployment in India", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button23 = ttk.Button(self,text = "Back To Home", command = lambda : controller.show_frame(StartPage))
        button23.pack()
        f =  Figure(figsize = (10,6), dpi = 100)
        a = f.add_subplot(111)
        a.set_title("It is showing that the number of people with Main activity as Households are high in the state of Uttar Pradesh with above 30 million people.")
        x = df["State"]
        y = df["Main Activity Household Duties - PersonsTotal"]        
        a.bar(x,y,color ='green')
        a.set_xlabel('State')
        a.set_ylabel('Main Activity Household Duties - PersonsTotal')
        a.tick_params(labelrotation=38)
        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class PageEleven(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Main Activity Beggars, Vagrants etc. - PersonsTotal", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button24 = ttk.Button(self,text = "Back To Home", command = lambda : controller.show_frame(StartPage))
        button24.pack()
        f =  Figure(figsize = (10,6), dpi = 60)
        a = f.add_subplot(111)
        a.set_title("It is evident that the number of people with Main activity as Beggars are high in the state of West of Bengal with above 70k people.")
        x = df["State"]
        y = df["Main Activity Beggars, Vagrants etc. - PersonsTotal"]
        a.clear()
        a.bar(x, y, color='blue')
        a.set_xlabel('State')
        a.set_ylabel('Main Activity Beggars, Vagrants etc. - PersonsTotal')
        a.tick_params(labelrotation=38)
        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class PageTwelve(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Relationship between No. of illiterate non workers and No of people in 100 thousands who are below Poverty Line for all states", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button25 = ttk.Button(self,text = "Back To Home", command = lambda : controller.show_frame(StartPage))
        button25.pack()
        f =  Figure(figsize = (10,6), dpi = 100)
        a = f.add_subplot(111)
        a.set_title("The graph shows that there's a very high positive association between  a states Non working illiterate people’s count and the No of people below poverty Line in it.")
        x = df['Non-Workers - PersonsIlliterate']
        y = df['No.ofPersons(lakhs) (Total)']
        a.clear()
        a.scatter(x, y, color='blue')
        a.set_xlabel('Non-Workers - PersonsIlliterate')
        a.set_ylabel('No.ofPersons(lakhs) (Total)')
        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class PageThirteen(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Relationship between No. of literate non workers and No of people in 100 thousands who are below Poverty Line for all states", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button26 = ttk.Button(self,text = "Back To Home", command = lambda : controller.show_frame(StartPage))
        button26.pack()
        f =  Figure(figsize = (10,6), dpi = 100)
        a = f.add_subplot(111)
        a.set_title("Even the plot between the Illiterate Non workers and No of People below poverty line tend to have a high association with each other")
        x = df['Non-Workers - PersonsLiterate']
        y = df['No.ofPersons(lakhs) (Total)']
        a.clear()
        a.scatter(x, y, color='red')
        a.set_xlabel('Non-Workers - PersonsLiterate')
        a.set_ylabel('No.ofPersons(lakhs) (Total')
        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

app = dab203app()
app.geometry("1280x720")
app.state("zoomed")
app.mainloop()
