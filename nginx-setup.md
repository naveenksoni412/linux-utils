Run this:

```
sudo apt install nginx -y

sudo vi /etc/nginx/sites-available/nke-apps
```

paste these contents [configs/nke_apps]

```
sudo ln -s /etc/nginx/sites-available/nke-apps /etc/nginx/sites-enabled/
sudo service nginx restart

```
