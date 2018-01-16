from flask import Flask, render_template, request


import DBcm


app = Flask(__name__)


config = {
    'host': '127.0.0.1',
    'database': 'alertDB',
    'user': 'user',
    'password': 'password',
}


@app.route('/')
@app.route('/alert')
def get_alert():
    return render_template('get_alert.html')


@app.route('/put_alert', methods=['POST'])
def put_alert():
    _id = request.form['id']
    alert = request.form['alert']
    with DBcm.UseDatabase(config) as cursor:
        _SQL = """insert into alerts
                  (alert_id, alert_text)
                  values
                  (%s, %s)"""
        cursor.execute(_SQL, (_id, alert))
    return "Thanks for the alert!"


@app.route('/showalerts')
def show_all_alerts():
    with DBcm.UseDatabase(config) as cursor:
        _SQL = """select * from alerts"""
        cursor.execute(_SQL)
        data = cursor.fetchall()
    return render_template('showthealerts.html',
                           the_data=data) 


if __name__ == '__main__':
    app.run(debug=True)
