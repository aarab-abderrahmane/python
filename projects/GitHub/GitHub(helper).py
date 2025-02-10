import subprocess
import os


def status():
    try:
        result=subprocess.run(['git','status','--porcelain'],capture_output=True,text=True)
        if result.returncode==0:
            if not result.stdout.strip():
                return True , 'not change'
            else:
                changes=result.stdout.strip().split('\n')
                changes_list=[change[3:].strip() for change in changes]  # change this 
                print(f"there are changes not yet staged for commit : \n"+"\n".join(changes_list))
                return True 
        else:
            return False , 'error'
    except subprocess.CalledProcessError:
        return False
    

def check_git_installed():
    try:
        result=subprocess.run(['git', '--version'], check=True, capture_output=True, text=True)
        if result.returncode==0:
         return True
        
        else:
            return False ,"something is wrong"
        
    except subprocess.CalledProcessError:
        return False
    

def show_files(name_repo):
    os.chdir(name_repo)
    # print("Successfully navigated!")
    # print(f"Current working directory: {os.getcwd()}")
    print("\n==files==")
    show_files = subprocess.run(['ls'], capture_output=True, text=True)  
    show_files=show_files.stdout.replace('  ','\n')
    print(show_files)


def clone():
    url = input('Enter URL of the repository: ').strip()
    result = subprocess.run(['git', 'clone', url], capture_output=True, text=True)

    if result.returncode == 0:
        name_repo = url.split('/')[-1].replace('.git', '')
        print(result.stdout)

        try:
            show_files(name_repo)
            return True

        except Exception as e:
            print(f"Error navigating to the repository directory: {e}")
            return False

    else:
        error_message = result.stderr.lower()
        if "already exists and is not an empty directory" in error_message:
            print("Error: The repository already exists in the current directory.")
            name_repo = url.split('/')[-1].replace('.git', '')
            show_files(name_repo)
            return True
        
        elif "not found" in error_message or "does not exist" in error_message:
            print("Error: The URL provided is incorrect or the repository does not exist.")
        elif "permission denied" in error_message:
            print("Error: Permission denied. Check your access rights to the repository.")
        elif "early eof" in error_message or "rpc failed" in error_message:
            print("Error: Network issue occurred while cloning the repository. Please check your internet connection.")
        else:
            print("An unknown error occurred:")
            print(result.stderr)
        
        return False


def check_name_email():
    try:
        username=subprocess.check_output(['git','config','--global','user.name'],text=True).strip()
        email_process=subprocess.check_output(['git','config','--global','user.email'],text=True).strip()

        return True , 'Username and email already exist'
   
    except subprocess.CalledProcessError:
        name=input("type your name : ").strip()
        email=input("type your email : ").strip()
        username=subprocess.run(['git','config','--global','user.name',name],capture_output=True,text=True)
        email_process=subprocess.run(['git','config','--global','user.email',email],capture_output=True,text=True)
        
        if username.returncode==0 and email_process.returncode==0:
            return True
        
        else:
            return False
        # if username.stderr: return False

        # if email_process.stderr : return False

        # if "@" not in email or 'gmail.' not in email.split('@')[-1]: return False


def add_to_git():
    try:
        empty=0
        change_name=input('enter name file (add comma) : ').strip().split(',')
        for i in change_name:
          result=subprocess.run(['git','add',i],capture_output=True,text=True)

          if result.returncode == 0: 
                empty+=1
        
        if empty==len(change_name):
            print('successfully')
            return True
        
        elif 1<=empty<len(change_name):
            print('There are files that have not been added')
            return True
        
        else:
            # if "did not match any files" in result.stderr: return False
            return False
        
    except subprocess.CalledProcessError: return False

def add_commit():
    try:
        commit=input('type commit message : ').strip()
        if commit!="":
            result=subprocess.run(['git','commit','-m',commit],capture_output=True,text=True)
            if result.returncode == 0 : 
                return True
            else:
                return False
        else:
            return False
    except subprocess.CalledProcessError:
        return False
# _________________________________________________________________________________
def github_helper():
    if check_git_installed():
        
        if check_name_email():
            print(check_name_email())
            if clone():
                if status():
                    if add_to_git():
                        if add_commit():
                            subprocess.run(['git','push'])
                        else:
                            return
                    else:
                        return
                else:
                    return 
        else:
            return

    else:
        return

github_helper()