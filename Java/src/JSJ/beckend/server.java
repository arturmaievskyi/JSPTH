
import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;

import java.io.OutputStream;
import java.io.IOException;
import java.net.InetSocketAddress;
import java.util.HashMap;
import java.util.Map;

// Request Class
class Request {
    private final HttpExchange exchange;

    public Request(HttpExchange exchange) {
        this.exchange = exchange;
    }

    public String getMethod() {
        return exchange.getRequestMethod();
    }

    public String getPath() {
        return exchange.getRequestURI().getPath();
    }

    public String getQuery() {
        return exchange.getRequestURI().getQuery();
    }

    public String getBody() throws IOException {
        return new String(exchange.getRequestBody().readAllBytes());
    }
}

// Response Class
class Response {
    private final HttpExchange exchange;

    public Response(HttpExchange exchange) {
        this.exchange = exchange;
    }

    public void send(String body, int statusCode) throws IOException {
        exchange.sendResponseHeaders(statusCode, body.getBytes().length);
        OutputStream os = exchange.getResponseBody();
        os.write(body.getBytes());
        os.close();
    }
}

// Handler Interface
interface Handler {
    void handle(Request req, Response res) throws IOException;
}

// Router Class
class Router {
    private final Map<String, Handler> routes = new HashMap<>();

    public void addRoute(String path, Handler handler) {
        routes.put(path, handler);
    }

    public Handler resolve(String path) {
        return routes.getOrDefault(path, (req, res) -> res.send("404 Not Found", 404));
    }
}


public class MiniWebFramework {
    private final HttpServer server;
    private final Router router = new Router();

    public MiniWebFramework(int port) throws IOException {
        server = HttpServer.create(new InetSocketAddress(port), 0);
        server.createContext("/", (exchange) -> {
            Request req = new Request(exchange);
            Response res = new Response(exchange);

            Handler handler = router.resolve(req.getPath());
            handler.handle(req, res);
        });
    }

    public void start() {
        System.out.println("Server is running...");
        server.start();
    }

    public void addRoute(String path, Handler handler) {
        router.addRoute(path, handler);
    }
}