with open("access_log.micro") as f:
    lines = f.read().splitlines()

for line in lines:
    fields = line.split('"')

    ip_date = fields[0].split()
    ipaddr = ip_date[0]
    date = " ".join(ip_date[3:5])

    method, path, http_version = fields[1].split()

    code_byte = fields[2].split()
    status_code = code_byte[0].strip()
    response_bytes = code_byte[1].strip()

    user_agent = fields[6]

    print(
        ipaddr,
        date,
        method,
        path,
        http_version,
        status_code,
        response_bytes,
        user_agent,
    )
