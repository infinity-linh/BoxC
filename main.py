import os

os.system("pip install packaging")
os.system("pip install -r requirements.txt")
# os.system("conda create --name box_c --file environment_my_islle.tar.gz")

import chapter.main_window.main_page
# import login.login_page


if __name__ == "__main__":
    # app = login.login_page.App()
    app = chapter.main_window.main_page.App_main()
    app.mainloop()