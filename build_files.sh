echo " BUILD START"
python3 -m pip install -r requirement.txt
python3 manage.py collectstatic --noinput --clear
echo " BUILD END"
