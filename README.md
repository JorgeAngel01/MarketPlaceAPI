```
python -m venv venv
```
```
Set-ExecutionPolicy Unrestricted -Scope Process
```
```
venv\Scripts\activate
```
```
pip install -r requirements.txt
```
```
cd marketplace
```
```
python manage.py migrate
```
```
python manage.py createsuperuser
```
