app = "rage-sniper-k7asug"

kill_signal = "SIGINT"
kill_timeout = 5
processes = []

[build]
  dockerfile = "Dockerfile"

[env]
  PORT = "8080"

[http_service]
  internal_port = 8080
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true
  min_machines_running = 1

  [[http_service.ports]]
    handlers = ["http"]
    port = 80

  [[http_service.ports]]
    handlers = ["tls", "http"]
    port = 443
