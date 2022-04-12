from opentelemetry import trace
from opentelemetry.instrumentation import tornado
from opentelemetry.instrumentation.tornado import TornadoInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor


import tornado.web
from opentelemetry.instrumentation.tornado import TornadoInstrumentor

# apply tornado instrumentation
TornadoInstrumentor().instrument()

class Handler(tornado.web.RequestHandler):
    def get(self):
        self.set_status(200)

app = tornado.web.Application([(r"/", Handler)])
app.listen(8080)
tornado.ioloop.IOLoop.current().start()