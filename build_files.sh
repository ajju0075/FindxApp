
echo " BUILD START"
python3.10.7 -m pip install requirments.txt
python3.10.7 manage.py clollectstatic --noinput --clear
echo " BUILD END"
