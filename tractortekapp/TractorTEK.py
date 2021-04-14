from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms_sqlalchemy.fields import QuerySelectField
import os
from os.path import join, dirname, realpath
import pandas as pd
import sqlalchemy
from datetime import date
from wtforms.validators import DataRequired
from sqlalchemy.exc import DataError, IntegrityError



app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:reyansh123@localhost:3306/mayekar_py_capstone"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

# SQL DATABASE AND MODELS
# Class Sales Team
class sales_team(db.Model):
    __tablename__ = 'sales_team'
    emp_id = db.Column(db.String(10), primary_key=True)
    sales_team_lead = db.Column(db.String(50))
    paygrade = db.Column(db.String(5))
    region = db.Column(db.String(5))

    def __init__(self,emp_id,sales_team_lead,paygrade,region):
        self.emp_id = emp_id
        self.sales_team_lead = sales_team_lead
        self.paygrade = paygrade
        self.region = region

    def __repr__(self):
        return f"emp_id: {self.emp_id}  sales_team_lead: {self.sales_team_lead}  paygrade  :{self.paygrade}  region : {self.region} "

# Class product
class product(db.Model):
    __tablename__ = 'product'
    prod_code = db.Column(db.String(10), primary_key = True)
    prod_name = db.Column(db.String(50))
    url =db.Column(db.String(200))
    link =db.Column(db.String(100))
    manufacturer =db.Column(db.String(20))
    extended_service_plan = db.Column(db.String(10))
    warranty_price =db.Column(db.Integer)


    def __init__(self,prod_code,prod_name,url,link,manufacturer,extended_service_plan,warranty_price):
        self.prod_code = prod_code
        self.prod_name = prod_name
        self.url = url
        self.link = link
        self.manufacturer = manufacturer
        self.extended_service_plan = extended_service_plan
        self.warranty_price=warranty_price


    def __repr__(self):
        return f"prod_code :{self.prod_code} prod_name: {self.prod_name}  url : {self.url}  manufacturer : {self.manufacturer}  extended_service_plan : {self.extended_service_plan}   "



class quarter_price(db.Model):
    __tablename__ = 'quarter_price'
    srno = db.Column(db.Integer, primary_key=True)
    prod_code = db.Column(db.String(10), db.ForeignKey("product.prod_code"))
    quarter = db.Column(db.String(10))
    price =db.Column(db.Integer)


    def __init__(self,prod_code,quarter,price):
        self.prod_code=prod_code
        self.quarter = quarter
        self.price = price

    def __repr__(self):
        return f"prod_code :{self.prod_code} Quarter: {self.quarter}  Price : {self.price}  "


#Class Sales
class sales(db.Model):
    __tablename__ = 'sales'
    sales_id = db.Column(db.Integer, primary_key = True)
    emp_id = db.Column(db.String(10), db.ForeignKey("sales_team.emp_id"))
    yr = db.Column(db.String(5))
    wk = db.Column(db.String(5))
    quarter = db.Column(db.String(10))
    prod_code = db.Column(db.String(10), db.ForeignKey("product.prod_code"))
    prod_qty = db.Column(db.Integer)
    esp = db.Column(db.String(10))
    esp_num=db.Column(db.Integer)

    def __init__(self,emp_id,yr,wk,quarter,prod_code,prod_qty,esp,esp_num):
        self.emp_id = emp_id
        self.yr = yr
        self.wk = wk
        self.quarter=quarter
        self.prod_code = prod_code
        self.prod_qty = prod_qty
        self.esp= esp
        self.esp_num = esp_num

    def __repr__(self):
        return f"sales_id :{self.sales_id} "


#Class Sales sales_history
class sales_history(db.Model):
    __tablename__ = 'sales_history'
    SrNo = db.Column(db.Integer, primary_key=True)
    item_code = db.Column(db.String(10))
    emp_id =db.Column(db.String(10))
    year = db.Column(db.Integer)
    w0 = db.Column(db.Integer)
    w1 = db.Column(db.Integer)
    w2 = db.Column(db.Integer)
    w3 = db.Column(db.Integer)
    w4 = db.Column(db.Integer)
    w5 = db.Column(db.Integer)
    w6 = db.Column(db.Integer)
    w7 = db.Column(db.Integer)
    w8 = db.Column(db.Integer)
    w9 = db.Column(db.Integer)
    w10 = db.Column(db.Integer)
    w11 = db.Column(db.Integer)
    w12 = db.Column(db.Integer)
    w13 = db.Column(db.Integer)
    w14 = db.Column(db.Integer)
    w15 = db.Column(db.Integer)
    w16 = db.Column(db.Integer)
    w17 = db.Column(db.Integer)
    w18 = db.Column(db.Integer)
    w19 = db.Column(db.Integer)
    w20 = db.Column(db.Integer)
    w21 = db.Column(db.Integer)
    w22 = db.Column(db.Integer)
    w23 = db.Column(db.Integer)
    w24 = db.Column(db.Integer)
    w25 = db.Column(db.Integer)
    w26 = db.Column(db.Integer)
    w27 = db.Column(db.Integer)
    w28 = db.Column(db.Integer)
    w29 = db.Column(db.Integer)
    w30 = db.Column(db.Integer)
    w31 = db.Column(db.Integer)
    w32 = db.Column(db.Integer)
    w33 = db.Column(db.Integer)
    w34 = db.Column(db.Integer)
    w35 = db.Column(db.Integer)
    w36 = db.Column(db.Integer)
    w37 = db.Column(db.Integer)
    w38 = db.Column(db.Integer)
    w39 = db.Column(db.Integer)
    w40 = db.Column(db.Integer)
    w41 = db.Column(db.Integer)
    w42 = db.Column(db.Integer)
    w43 = db.Column(db.Integer)
    w44 = db.Column(db.Integer)
    w45 = db.Column(db.Integer)
    w46 = db.Column(db.Integer)
    w47 = db.Column(db.Integer)
    w48 = db.Column(db.Integer)
    w49 = db.Column(db.Integer)
    w50 = db.Column(db.Integer)
    w51 = db.Column(db.Integer)

    def __init__(self,item_code,emp_id,year,w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,w23,w24,w25,w26,w27,w28,w29,w30,w31,w32,w33,w34,w35,w36,w37,w38,w39,w40,w41,w42,w43,w44,w45,w46,w47,w48,w49,w50,w51):
        self.item_code = item_code
        self.emp_id = emp_id
        self.year = year
        self.w0 = w0
        self.w1 = w1
        self.w2 = w2
        self.w3= w3
        self.w4 = w4
        self.w5 = w5
        self.w6 = w6
        self.w7 = w7
        self.w8= w8
        self.w9 = w9
        self.w10 = w10
        self.w11 = w11
        self.w12 = w12
        self.w13= w13
        self.w14 = w14
        self.w15 = w15
        self.w16 = w16
        self.w17 = w17
        self.w18= w18
        self.w19 = w19
        self.w20 = w20
        self.w21 = w21
        self.w22 = w22
        self.w23= w23
        self.w24 = w24
        self.w25 = w25
        self.w26 = w26
        self.w27 = w27
        self.w28= w28
        self.w29 = w29
        self.w30 = w30
        self.w31 = w31
        self.w32 = w32
        self.w33= w33
        self.w34 = w34
        self.w35 = w35
        self.w36 = w36
        self.w37 = w37
        self.w38= w38
        self.w39 = w39
        self.w40 = w40
        self.w41 = w41
        self.w42 = w42
        self.w43= w43
        self.w44 = w44
        self.w45 = w45
        self.w46 = w46
        self.w47 = w47
        self.w48= w48
        self.w49 = w49
        self.w50 = w50
        self.w51 = w51

    def __repr__(self):
        return f"item_code :{self.item_code}"




# Flask Form

class AddForm(FlaskForm):
    emp_id = StringField('Sales Team Lead:')
    yr=StringField('Year:')
    wk=StringField('Week:')
    quarter=StringField('Quarter:')
    prod_code=StringField('Prod code')
    prod_qty=IntegerField('Product Quantity:')
    esp=StringField('Extended Service Plan')
    esp_num=IntegerField('ESP Quantity:')
    submit = SubmitField('Add Sales Data')


# Flask Views

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/fail')
def fail():
    return render_template('fail.html')


@app.route('/salesdata', methods=['GET', 'POST'])
def new_sales():
    form = AddForm()
    if form.validate_on_submit():
        emp_id= form.emp_id.data
        yr= form.yr.data
        wk= form.wk.data
        quarter= form.quarter.data
        prod_code= form.prod_code.data
        prod_qty= form.prod_qty.data
        esp= form.esp.data
        esp_num= form.esp_num.data
        weeksales = sales(emp_id,yr,wk,quarter,prod_code,prod_qty,esp,esp_num)
        try:
            db.session.add(weeksales)
            db.session.commit()
            return redirect(url_for('success'))
        except IntegrityError:
            db.session.rollback()
            return redirect(url_for('fail'))

    return render_template('salesdata.html',form=form)


############################
#Restore sales team data
###########################

# upload folders for csv

UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER


@app.route('/upsalesteam')
def upsalesteam():
     # Set The upload HTML template '\templates\index.html'
    return render_template('upsalesteam.html')

@app.route("/upsalesteam", methods=['POST'])

def uploadFiles():
      # get the uploaded file
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)
           parseCSV(file_path)
          # save the file
#      return redirect(url_for('index'))
      return render_template('success.html')

def parseCSV(file_path):
      # CVS Column Names
      col_names = ['emp_id','sales_team_lead', 'paygrade','region']
      # Use Pandas to parse the CSV file
      csvData = pd.read_csv(file_path,names=col_names, header=None)
      # Loop through the Rows
      for i,row in csvData.iterrows():
          emp_id = (row['emp_id'])
          sales_team_lead = (row['sales_team_lead'])
          paygrade = (row['paygrade'])
          region = (row['region'])
          Addsalesteam = sales_team(emp_id,sales_team_lead,paygrade,region)

          db.session.add(Addsalesteam)
          db.session.commit()


############################
#Restore Product Data
###########################

@app.route('/uproduct')
def uproduct():
     # Set The upload HTML template '\templates\index.html'
    return render_template('uproduct.html')

@app.route("/uproduct", methods=['POST'])
def uploadFiles1():
      # get the uploaded file
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)
           parseCSV1(file_path)
          # save the file
#      return redirect(url_for('index'))
      return render_template('success.html')

def parseCSV1(file_path):
      # CVS Column Names
      col_names = ['prod_code','prod_name', 'url','link','manufacturer','extended_service_plan','warranty_price']
      # Use Pandas to parse the CSV file
      csvData = pd.read_csv(file_path,names=col_names, header=None)
      # Loop through the Rows
      for i,row in csvData.iterrows():
          prod_code = (row['prod_code'])
          prod_name = (row['prod_name'])
          url = (row['url'])
          link = (row['link'])
          manufacturer = (row['manufacturer'])
          extended_service_plan = (row['extended_service_plan'])
          warranty_price = (row['warranty_price'])

          Addproduct = product(prod_code,prod_name,url,link,manufacturer,extended_service_plan,warranty_price)
          db.session.add(Addproduct)
          db.session.commit()

@app.route('/uqprices')
def uqprices():
     return render_template('uqprices.html')

@app.route("/uqprices", methods=['POST'])
def uploadFiles4():
      # get the uploaded file
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)
           parseCSV4(file_path)
          # save the file
#      return redirect(url_for('index'))
      return render_template('success.html')

def parseCSV4(file_path):
      # CVS Column Names
      col_names = ['prod_code','quarter', 'price']
      # Use Pandas to parse the CSV file
      csvData = pd.read_csv(file_path,names=col_names, header=None)
      # Loop through the Rows
      for i,row in csvData.iterrows():
          prod_code = (row['prod_code'])
          quarter = (row['quarter'])
          price = (row['price'])

          qprice = quarter_price(prod_code,quarter,price)
          db.session.add(qprice)
          db.session.commit()


############################
#Restore Sales data
###########################

@app.route('/uploadsales')
def uploadsales():
     # Set The upload HTML template '\templates\index.html'
    return render_template('uploadsales.html')

@app.route("/uploadsales", methods=['POST'])
def uploadFiles5():
      # get the uploaded file
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)
           parseCSV5(file_path)
          # save the file
#      return redirect(url_for('index'))
      return render_template('success.html')

def parseCSV5(file_path):
      # CVS Column Names
      col_names = ['item_code', 'emp_id', 'year', 'w0', 'w1','w2','w3','w4','w5','w6','w7','w8','w9','w10','w11','w12','w13','w14','w15','w16','w17','w18','w19','w20','w21', 'w22','w23','w24','w25','w26','w27','w28','w29','w30','w31','w32','w33','w34','w35','w36','w37','w38','w39','w40','w41','w42','w43','w44','w45','w46','w47','w48','w49','w50','w51']
      # Use Pandas to parse the CSV file
      csvData = pd.read_csv(file_path,names=col_names, header=None)
      # Loop through the Rows
      for i,row in csvData.iterrows():
          item_code = (row['item_code'])
          emp_id = (row['emp_id'])
          year = (row['year'])
          w0 = (row['w0'])
          w1 = (row['w1'])
          w2 = (row['w2'])
          w3 = (row['w3'])
          w4 = (row['w4'])
          w5 = (row['w5'])
          w6 = (row['w6'])
          w7 = (row['w7'])
          w8 = (row['w8'])
          w9 = (row['w9'])
          w10 = (row['w10'])
          w11 = (row['w11'])
          w12 = (row['w12'])
          w13 = (row['w13'])
          w14 = (row['w14'])
          w15 = (row['w15'])
          w16 = (row['w16'])
          w17 = (row['w17'])
          w18 = (row['w18'])
          w19 = (row['w19'])
          w20 = (row['w20'])
          w21 = (row['w21'])
          w22 = (row['w22'])
          w23 = (row['w23'])
          w24 = (row['w24'])
          w25 = (row['w25'])
          w26 = (row['w26'])
          w27 = (row['w27'])
          w28 = (row['w28'])
          w29 = (row['w29'])
          w30 = (row['w30'])
          w31 = (row['w31'])
          w32 = (row['w32'])
          w33 = (row['w33'])
          w34 = (row['w34'])
          w35 = (row['w35'])
          w36 = (row['w36'])
          w37 = (row['w37'])
          w38 = (row['w38'])
          w39 = (row['w39'])
          w40 = (row['w40'])
          w41 = (row['w41'])
          w42 = (row['w42'])
          w43 = (row['w43'])
          w44 = (row['w44'])
          w45 = (row['w45'])
          w46 = (row['w46'])
          w47 = (row['w47'])
          w48 = (row['w48'])
          w49 = (row['w49'])
          w50 = (row['w50'])
          w51 = (row['w51'])

          Addsalesdata = sales_history(item_code, emp_id, year, w0, w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,w23,w24,w25,w26,w27,w28,w29,w30,w31,w32,w33,w34,w35,w36,w37,w38,w39,w40,w41,w42,w43,w44,w45,w46,w47,w48,w49,w50,w51)
          db.session.add(Addsalesdata)
          db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
