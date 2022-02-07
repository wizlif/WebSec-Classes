### Setup nginx
- Install nginx `sudo apt-get install nginx`
- Add nginx to the firewall `sudo ufw allow 'Nginx HTTP'`
- Flush iptable `iptables -F -t nat`

### Setup project
- Clone the repo `git clone https://github.com/wizlif/WebSec-Classes`
- Create a web hosting directory `/var/www/react`
- Copy the [index.html](index.html) to `/var/www/react`
- Copy [myreact.01.conf](myreact.01.conf) to `/etc/nginx/sites-available`
- Rename it to `myreact.conf`
- Enable the web configuration by creating a link in `sites-enabled` using `ln -s /etc/nginx/sites-available/myreact.conf /etc/nginx/sites-enabled/myreact.conf`
- Check if the configuration is valid `nginx -t`
- Failing configuration is due to clashing with `default` configuration.
- Disable it by deleting the `default` configuration from `nginx` with `rm -rf /etc/nginx/sites-enabled/default`
- Restart nginx `/etc/init.d/nginx restart` -OR- `systemctl restart nginx`
- Add `myreact.com` to `/etc/hosts` `127.0.0.1 myreact.com www.myreact.com`
- Attempt to load `myreact.com` in browser

### Generate self signed SSL
- Create an SSL key `openssl req -newkey rsa:4096 -x509 -sha256 -days 3650 -nodes -out myreact.crt -keyout myreact.key`

### Setup SSL
- As above, setup and enable the `myreact.ssl.conf`
- Edit `/etc/nginx/sites-available/myreact.conf` to match [myreact.02.conf](myreact.02.conf) so as to redirect to https.
- Test & restart nginx