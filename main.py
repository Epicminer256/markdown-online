import markdown
from markdown.extensions.tables import TableExtension
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
  if bool(request.args.get('md')) and bool(request.args.get('css')):
    genMarkdown = markdown.markdown(request.args.get('md'), extensions=[TableExtension(use_align_attribute=True)])
    return '<html><head><style>' + request.args.get('css') + '</style></head><body>' + genMarkdown + '</body></html>'
  return open('index.html', 'r').read()

# main driver function
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
