from flask import Flask, request, render_template
import numpy as np
import pickle
port = int(os.environ.get('PORT', 5000))


#import request

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')

def bet_result(w,v,p,d):
  Day_1 = 0
  Day_2 = 0
  Day_3 = 0
  Day_4 = 0
  Day_5 = 0
  Day_6 = 0
  Day_7 = 0
  Player_M = 0
  Player_N = 0
  Player_E =0
  Value = v
  if d == 1:
    Day_1 = 1
  elif d == 2:
    Day_2 = 1
  elif d == 3:
    Day_3 = 1
  elif d == 4:
    Day_4 = 1
  elif d == 5:
    Day_5 = 1
  elif d == 6:
    Day_6 = 1
  elif d == 7:
    Day_7 = 1
  else:
    0
    
  
  if p == 'M':
    Player_M = 1
  elif p == 'N':
    Player_N = 1
  elif p == 'E':
    Player_E = 1
  else:
    0
  result = model.predict([[w, Value,   Player_E,   Player_M,   Player_N,   Day_1,  Day_2,  Day_3,  Day_4,  Day_5,  Day_6,  Day_7]])
  #print([[Value,   Player_E,   Player_M,   Player_N,   Day_1,  Day_2,  Day_3,  Day_4,  Day_5,  Day_6,  Day_7]])
  print('Player ' + p + ' : ' + str(result))

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    w = request.form['week']
    v = request.form['value']
    p = request.form['player']
    d = request.form['day']
    Day_1 = 0
    Day_2 = 0
    Day_3 = 0
    Day_4 = 0
    Day_5 = 0
    Day_6 = 0
    Day_7 = 0
    Player_M = 0
    Player_N = 0
    Player_E =0
    Value = v
    if d == 1:
      Day_1 = 1
    elif d == 2:
      Day_2 = 1
    elif d == 3:
      Day_3 = 1
    elif d == 4:
      Day_4 = 1
    elif d == 5:
      Day_5 = 1
    elif d == 6:
      Day_6 = 1
    elif d == 7:
      Day_7 = 1
    else:
      0

    
    if p == 'M':
      Player_M = 1
    elif p == 'N':
      Player_N = 1
    elif p == 'E':
      Player_E = 1
    else:
      0
    result = model.predict([[w, Value,   Player_E,   Player_M,   Player_N,   Day_1,  Day_2,  Day_3,  Day_4,  Day_5,  Day_6,  Day_7]])
    #print([[Value,   Player_E,   Player_M,   Player_N,   Day_1,  Day_2,  Day_3,  Day_4,  Day_5,  Day_6,  Day_7]])
    #print('Player ' + p + ' : ' + str(result))

    #final_features = [np.array(int_features)]
    prediction = bet_result(w,v,p,d)

    output = prediction

    return render_template('index.html', prediction_text = 'Player ' + p + ' : ' + str(result))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)