#!/usr/bin/python3
import sys
import os
import psycopg2
import socket
from getpass import getpass
from tqdm import tqdm
from urllib.request import urlopen
import re

def title():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(nadpis)
    print(13 * " " + 50 * "_")
    print(30 * " " + "username:" + user)
    print(30 * " " +"host:" + host)
    print(30 * " " +"port:" + port)
    print(30 * " " +"schema:" + schema)
    print(13 * " " + 50 * "_")
    print("\n")
def check_sch(schema):
    try:
        cur.execute("select nspname from pg_catalog.pg_namespace;")
        sch = cur.fetchall()
        for i in sch:
            y = (f"{i}".replace("(", "").replace(")", "").replace(",", "").replace("'", ""))
            if y == schema:
                return "nice"
    except:
        return "error"

def add_URL(URL,Source):
    try:
        cur.execute("insert into URL (URL, Source) values (%s, %s)", (URL, Source))
        con.commit()
    except:
        print("it cannot be added into url table")

def add_IP(IP,Source):
    try:
        cur.execute("insert into IP (IP, Source) values (%s, %s)", (IP, Source))
        con.commit()
    except:
        print("it cannot be added into IP table")

def add_Master(URL, IP, Source):
    try:
        cur.execute("insert into Master (URL, IP, Source) values (%s, %s, %s)", (URL, IP, Source))
        con.commit()
    except:
        print("it cannot be added into Master table")

def urt_to_ip(url):
    url_split = url.split("/")
    if url_split[0] == "http:":
        try:
            return (socket.gethostbyname(url_split[2]))
        except:
            return "it cannot be converted into ip address"
    elif url_split[0] == "https:":
        try:
            return (socket.gethostbyname(url_split[2]))
        except:
            return "it cannot be converted into ip address"
    else:
        try:
            return (socket.gethostbyname(url_split[0]))
        except:
            return "it cannot be converted into ip address"

def find_url(string):
    regex = r"(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))"
    url = re.findall(regex, string)
    return url

def find_ip4(string):
    regex = "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    ip = re.findall(regex, string)
    return ip

def find_ip6(string):
    IPV4SEG = r'(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])'
    IPV4ADDR = r'(?:(?:' + IPV4SEG + r'\.){3,3}' + IPV4SEG + r')'
    IPV6SEG = r'(?:(?:[0-9a-fA-F]){1,4})'
    IPV6GROUPS = (
        r'(?:' + IPV6SEG + r':){7,7}' + IPV6SEG,
        r'(?:' + IPV6SEG + r':){1,7}:',
        r'(?:' + IPV6SEG + r':){1,6}:' + IPV6SEG,
        r'(?:' + IPV6SEG + r':){1,5}(?::' + IPV6SEG + r'){1,2}',
        r'(?:' + IPV6SEG + r':){1,4}(?::' + IPV6SEG + r'){1,3}',
        r'(?:' + IPV6SEG + r':){1,3}(?::' + IPV6SEG + r'){1,4}',
        r'(?:' + IPV6SEG + r':){1,2}(?::' + IPV6SEG + r'){1,5}',
        IPV6SEG + r':(?:(?::' + IPV6SEG + r'){1,6})',
        r':(?:(?::' + IPV6SEG + r'){1,7}|:)',
        r'fe80:(?::' + IPV6SEG + r'){0,4}%[0-9a-zA-Z]{1,}',
        r'::(?:ffff(?::0{1,4}){0,1}:){0,1}[^\s:]' + IPV4ADDR,
        r'(?:' + IPV6SEG + r':){1,4}:[^\s:]' + IPV4ADDR,
    )
    IPV6ADDR = '|'.join(['(?:{})'.format(g) for g in IPV6GROUPS[::-1]])  # Reverse rows for greedy match
    ip = re.findall(IPV6ADDR, string)
    return ip

def create_table_ip():
    try:
        cur.execute("CREATE TABLE IP (ID serial8,IP varchar(40),Source varchar(1000),PRIMARY KEY (ID)); ")
        con.commit()
    except:
        print("ip table cannot be created")

def create_table_url():
    try:
        cur.execute("CREATE TABLE URL (ID serial8,URL varchar(10000),Source varchar(1000),PRIMARY KEY (ID)); ")
        con.commit()

    except:
        print("url table cannot be created")

def create_table_MASTER():
    try:
        cur.execute("CREATE TABLE Master (ID serial8,URL varchar(10000),IP varchar(40),Source varchar(1000),PRIMARY KEY (ID)); ")
        con.commit()
    except:
        print("master table cannot be created")

def drop_table_ip():
    try:
        cur.execute("drop table IP; ")
        con.commit()
    except:
        print("ip table cannot be dropped")

def drop_table_master():
    try:
        cur.execute("drop table Master; ")
        con.commit()
    except:
        print("Master table cannot be dropped")

def drop_table_url():
    try:
        cur.execute("drop table URL; ")
        con.commit()
    except:
        print("URL table cannot be dropped")

def control_table_IP(schema):
    try:
        cur.execute("SELECT EXISTS ( SELECT FROM pg_catalog.pg_class c JOIN   pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE  n.nspname = %s AND c.relname = 'ip' AND c.relkind = 'r');" , (schema, ) )
        ip = cur.fetchone()
        for r in ip:
            cotrol = (f"{r}")
            if cotrol.lower() == "true":
                return "true"
            else:
                return "false"
    except:
        print("schema cannot be find or a lot of bad requests")


def control_table_URL(schema):
    try:
        cur.execute("SELECT EXISTS ( SELECT FROM pg_catalog.pg_class c JOIN   pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE  n.nspname = %s AND c.relname = 'url' AND c.relkind = 'r');" , (schema, ) )
        ip = cur.fetchone()
        for r in ip:
            cotrol = (f"{r}")
            if cotrol.lower() == "true":
                return "true"
            else:
                return "false"
    except:
        print("schema cannot be find or a lot of bad requests")

def control_table_MASTER(schema):
    try:
        cur.execute("SELECT EXISTS ( SELECT FROM pg_catalog.pg_class c JOIN   pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE  n.nspname = %s AND c.relname = 'master' AND c.relkind = 'r');" , (schema, ) )
        ip = cur.fetchone()
        for r in ip:
            cotrol = (f"{r}")
            if cotrol.lower() == "true":
                return "true"
            else:
                return "false"
    except:
        print("schema cannot be find or a lot of bad requests")

def control():
    control_ip = control_table_IP(schema)
    try:
        if control_ip.lower() == "false":
            print("you don't have ip table created ")
            print("press any button to create a table")
            print("press 99 to shut down the application")
            moznost = str(input("insert option: "))
            if moznost == "99":
                    cur.close()
                    con.close()
                    sys.exit()
            else:
                create_table_ip()
        control_url = control_table_URL(schema)
        if control_url.lower() == "false":
            print("you don't have url table created")
            print("press any button to create a table ")
            print("press 99 to shut down the application")
            moznost = str(input("insert option: "))
            if moznost == "99":
                    cur.close()
                    con.close()
                    sys.exit()
            else:
                create_table_url()
        control_master = control_table_MASTER(schema)
        if control_master.lower() == "false":
            print("you don't have master table created")
            print("press any button to create a table")
            print("press 99 to shut down the application")
            moznost = str(input("insert option: "))
            if moznost == "99":
                    cur.close()
                    con.close()
                    sys.exit()
            else:
                create_table_MASTER()
    except:
        print("schema cannot be find or a lot of bad requests")

def list_txt(Source):
    try:
        with open(Source) as infile:
            for line in tqdm(infile):
                url = find_url(line)
                for i in url:
                    ip = urt_to_ip(i)
                    add_URL(i, Source)
                    add_IP(ip, Source)
                    add_Master(i, ip, Source)
                y = find_ip4(line)
                for z in y:
                    add_IP(z, Source)
                    add_Master("NULL", z, Source)
                w = find_ip6(line)
                for wz in w:
                    add_IP(wz, Source)
                    add_Master("NULL", wz, Source)

    except:
        print("text file cannot be loaded")

def url_list(Source):
    try:
        lines = urlopen(Source)
        for line in tqdm(lines):
            line = line.rstrip()
            text = line.decode('utf-8')
            url = find_url(text)
            for i in url:
                ip = urt_to_ip(i)
                add_URL(i, Source)
                add_IP(ip, Source)
                add_Master(i, ip, Source)
            y = find_ip4(text)
            for z in y:
                add_IP(z, Source)
                add_Master("NULL", z, Source)
            w = find_ip6(text)
            for wz in w:
                add_IP(wz, Source)
                add_Master("NULL", wz, Source)
    except:
        print("url cannot be loaded")

def search_url(ip):
    cur.execute("select url from master where ip = %s ;", (ip,))
    l = cur.fetchall()
    for r in l:
        print(f"{r[0]} have address " + ip )

def end_option():
    print(50 * "_")
    print("press any button to continue to menu")
    print("press 99 to shut down the application")
    print(50 * "_")
    moznost = input("insert option: ")
    if moznost == "99":
        cur.close()
        con.close()
        sys.exit()
    else:
        title()

nadpis = """
                   ___          ___                     ___
                  (   )        (   )                   (   )
 ___  ___ ___ .-.  | |    .--.  | | .-.   .--.    .--.  | |   ___   .--.  ___ .-.
(   )(   |   )   \ | |   /    \ | |/   \ /    \  /    \ | |  (   ) /    \(   )   
 | |  | | | ' .-. ;| |  |  .-. ;|  .-. .|  .-. ;|  .-. ;| |  ' /  |  .-. ;| ' .-. ;
 | |  | | |  / (___) |  |  |(___) |  | ||  | | ||  |(___) |,' /   |  | | ||  / (___)
 | |  | | | |      | |  |  |    | |  | ||  |/  ||  |    | .  '.   |  |/  || |
 | |  | | | |      | |  |  | ___| |  | ||  ' _.'|  | ___| | `. \  |  ' _.'| |
 | |  ; ' | |      | |  |  '(   ) |  | ||  .'.-.|  '(   ) |   \ \ |  .'.-.| |
 ' `-'  / | |      | |  '  `-' || |  | |'  `-' /'  `-' || |    \ .'  `-' /| |
  '.__.' (___)    (___)  `.__,'(___)(___)`.__.'  `.__,'(___ ) (___)`.__.'(___)


                                                         Prager Tomáš

"""

print(nadpis)
print(50*"_")
print(13*" " + "login into the database")
print(50*"_")

user = ""
password = ""
host = ""
port = ""
dbname = ""
schema = ""

while True:
    user = str(input("insert username: "))
    password = getpass("insert password: ")
    host = str(input("insert servers ip address: "))
    port = str(input("insert servers port: "))
    dbname = str(input("insert database name: "))
    schema = str(input("insert database schema: "))
    try:
        psycopg2.connect(
            dbname=dbname, user=user, host=host, password=password, port=port)
        break

    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(nadpis)
        print(50 * "_")
        print("login into the database has failed")
        print(50 * "_")
        continue

con = psycopg2.connect(
          dbname=dbname, user=user, host=host, password=password, port=port)
cur = con.cursor()

while True:
    t = check_sch(schema)
    if t == "nice":
        break
    else:
        print("invalid schema")
        schema = str(input("insert database schema: "))

os.system('cls' if os.name == 'nt' else 'clear')

title()

moznost = ""
while True:
    print("#1 manually write url into the table")
    print("#2 insert text file with url into table")
    print("#3 insert urls from the url into your dabatase")
    print("#4 creates needed tables")
    print("#5 delete tables")
    print("#6 search")
    print("#99 shut down the application")
    try:
        moznost = str(input("insert option: "))
    except:
        print("\n")
    if moznost == "1":
        control()
        url = str(input("please pass url: "))
        for i in find_url(url):
            if len(i) == 0:
                print("cannot find url " + url)
            else:
                ip = urt_to_ip(i)

                if ip == "it cannot be converted into ip address":
                    print(ip + " " + i)
                else:
                    add_URL(i, "added from application")
                    add_IP(ip, "added from application")
                    add_Master(i, ip, "added from application")
        end_option()

    elif moznost == "2":
        control()
        x = str(input("insert path to your file: "))
        list_txt(x)
        end_option()

    elif moznost == "3":
        control()
        y = str(input("please pass url: "))
        url_list(y)
        end_option()


    elif moznost == "4":
        control_ip = control_table_IP(schema)
        if control_ip.lower() == "true":
            print("ip table already exists")
        elif control_ip.lower() == "false":
            create_table_ip()
        control_url = control_table_URL(schema)
        if control_url.lower() == "true":
            print("url table already exists")
        elif control_url.lower() == "false":
                create_table_url()
        control_master = control_table_MASTER(schema)
        if control_master.lower() == "true":
            print("master table already exists")
        elif control_master.lower() == "false":
            create_table_MASTER()
        end_option()

    elif moznost == "5":
        control_ip = control_table_IP(schema)
        if control_ip.lower() == "true":
            drop_table_ip()
        elif control_ip.lower() == "false":
            print("the table does not exist")
        control_url = control_table_URL(schema)
        if control_url.lower() == "true":
            drop_table_url()
        elif control_url.lower() == "false":
            print("the table does not exist")
        control_master = control_table_MASTER(schema)
        if control_master.lower() == "true":
            drop_table_master()
        elif control_master.lower() == "false":
            print("the table does not exist")
        end_option()

    elif moznost == "6":
        control_master = control_table_MASTER(schema)
        if control_master.lower() == "true":
            print("#1 search by using url")
            print("#2 search by using ip address")
            while True:
                moznost = str(input("insert option:"))
                if moznost == "1":
                    url = str(input("insert url: "))
                    ip = urt_to_ip(url)
                    search_url(ip)
                    break
                elif moznost == "2":
                    ip = str(input("insert ip adress: "))
                    search_url(ip)
                    break
                else:
                    print("invalid input")
                    continue
        else:
            print("master table hasnt been found")
        end_option()

    elif moznost == "99":
        cur.close()
        con.close()
        sys.exit()
