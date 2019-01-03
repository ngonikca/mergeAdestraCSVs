import os, subprocess, sys, webbrowser, pyperclip, datetime

numdays = int(sys.argv[2])
first_date_str = sys.argv[1]
first_date_obj = datetime.datetime.strptime(first_date_str, '%Y-%m-%d').date()
date_list = [first_date_obj + datetime.timedelta(days=x) for x in range(0, numdays)]

for date in date_list:
    print("Downloading " + str(date) + "...")
    url = 'https://app.adestra.com/Consumeraffairs/workspace/9/data/coretable/1/dataviewer?cxt_data_table_browse_download=csv&dataviewer_field=1.email%2C1.accredited_category%2C1.address%2C1.address1%2C1.source&dataviewer_filter=%7B%22type%22%3A%22Logic.Container%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22Rule.ContactDate.Created%22%2C%22negate%22%3A%7B%22negate%22%3Afalse%2C%22type%22%3A%22Type.Negate%22%7D%2C%22start_date%22%3A%7B%22type%22%3A%22Type.Date.Absolute%22%2C%22date%22%3A%22' + str(date) + '%22%7D%2C%22end_date%22%3A%7B%22type%22%3A%22Type.Date.Absolute%22%2C%22date%22%3A%22' + str(date) + '%22%7D%7D%5D%7D'
    pyperclip.copy(str(date))
    webbrowser.open(url)
    input("Press Enter to continue...")

print("Please merge the files with mergeAdestraCSVs.py.")