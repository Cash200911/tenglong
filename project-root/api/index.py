from flask import Flask, render_template, send_from_directory, url_for
from datetime import datetime

app = Flask(__name__, static_folder='../static', template_folder='../templates')

@app.route('/')
def index():
    page_url = url_for('index', _external=True)
    return render_template('index.html',
        title="腾龙娱乐 - 畅玩无限",
        description="腾龙娱乐 – 提供一流的线上娱乐服务。加入我们，享受极致体验！",
        page_url=page_url,
        now=datetime.utcnow().year
    )

@app.route('/robots.txt')
def robots():
    return send_from_directory(app.static_folder, 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(app.static_folder, 'sitemap.xml')

if __name__ == '__main__':
    app.run()
