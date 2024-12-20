from flask import Flask, jsonify, request
from flask_cors import CORS
import pymysql
from db_config import db_config

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return '¡Hola, mundo! esta es la API - Si ves esto es que estoy en servicio. No se supone que me debas acceder directamente :D.- Grav'

# Ruta Endpoint para obtener datos del total de suicidios por año
@app.route("/api/suicidios", methods=["GET"])
def get_suicidios():
    year = request.args.get("year", type=int)
    if not year:
        return jsonify({"error": "Falta el parámetro 'year'"}), 400

    try:
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()

        query = """
            SELECT a.Entidad, a.%s_Total, u.Latitud, u.Longitud
            FROM ambos AS a
            LEFT JOIN ubicaciones AS u ON a.Entidad = u.Entidad
            WHERE u.Latitud IS NOT NULL;
        """
        cursor.execute(query, (year,))
        results = cursor.fetchall()

        data = [
            {
                "Entidad": row[0],
                "Total": row[1],
                "Lat": row[2],
                "Lon": row[3]
            }
            for row in results
        ]
        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Ruta para obtener la distribución de métodos de suicidio
@app.route("/api/methods", methods=["GET"])
def get_methods():
    try:
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()

        query = """
            SELECT Metodo, COUNT(*) AS Total
            FROM suicidios
            GROUP BY Metodo;
        """
        cursor.execute(query)
        results = cursor.fetchall()

        data = [{"method": row[0], "count": row[1]} for row in results]
        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Ruta para obtener los suicidios por año
@app.route("/api/suicidios_por_agnio", methods=["GET"])
def get_suicidios_por_agnio():
    try:
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()

        query = """
            SELECT a.Entidad, a.2021_Total, a.2022_Total, a.2023_Total
            FROM ambos AS a
            WHERE a.2021_Total IS NOT NULL OR a.2022_Total IS NOT NULL OR a.2023_Total IS NOT NULL;
        """
        cursor.execute(query)
        results = cursor.fetchall()

        data = [
            {
                "Entidad": row[0],
                "2021": row[1],
                "2022": row[2],
                "2023": row[3]
            }
            for row in results
        ]
        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Endpoint para la gráfica de Barchart
@app.route("/api/suicidios_por_anio", methods=["GET"])
def get_suicidios_por_anio():
    try:
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()

        query = """
            SELECT Entidad, 
                   2021_Total, 2022_Total, 2023_Total
            FROM ambos
            WHERE 2021_Total IS NOT NULL OR 2022_Total IS NOT NULL OR 2023_Total IS NOT NULL;
        """
        cursor.execute(query)
        results = cursor.fetchall()

        data = [
            {
                "Entidad": row[0],
                "2021": row[1],
                "2022": row[2],
                "2023": row[3]
            }
            for row in results
        ]
        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Endpoint para la gráfica de Linechart
@app.route("/api/metodos_por_anio", methods=["GET"])
def get_metodos_por_anio():
    try:
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()

        query = """
            SELECT Metodo, 
                   SUM(2010_Total), SUM(2011_Total), SUM(2012_Total), 
                   SUM(2013_Total), SUM(2014_Total), SUM(2015_Total), 
                   SUM(2016_Total), SUM(2017_Total), SUM(2018_Total),
                   SUM(2019_Total), SUM(2020_Total), SUM(2021_Total),
                   SUM(2022_Total), SUM(2023_Total)
            FROM metodos
            GROUP BY Metodo;
        """
        cursor.execute(query)
        results = cursor.fetchall()

        data = [
            {
                "Metodo": row[0],
                "Totales": row[1:]  # Todos los totales por año
            }
            for row in results
        ]
        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Endpoint para la gráfica de Piechart
@app.route("/api/metodos_2023", methods=["GET"])
def get_metodos_2023():
    try:
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()

        query = """
            SELECT Metodo, 2023_Total
            FROM metodos
            WHERE 2023_Total IS NOT NULL;
        """
        cursor.execute(query)
        results = cursor.fetchall()

        data = [
            {
                "Metodo": row[0],
                "2023": row[1]
            }
            for row in results
        ]
        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
