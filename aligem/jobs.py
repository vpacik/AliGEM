# Jobs handling suite

import subprocess
import argparse

def main() :
    pass

def get_jobs(user,verbose=False) :
    """ Return output of alien_top as a single string"""
    # TODO: ATM it is handled by try-except clause, a Popen might be more suitable (and stable?) solution
    try :
        output = subprocess.check_output(['alien_top','-all_status','-user',str(user)])
        return output
    except subprocess.CalledProcessError as error :
        if(verbose) :
            print("CalledProcessError caught!")
            print("Error return code:\n" + str(error.returncode))
            print("Error cmd:\n" + str(error.cmd))
            print("Error output:\n" + str(error.output))
        return error.output

def get_job_list(list='') :
    """ Returns list of job dicts from single string output """
    # stripping useless characters within jobs output
    list = list.replace(" ","") # removing whitespaces
    list = list.rstrip("\n\n") # stripping last \n\n to avoid empty entries
    jobs = list.split("\n\n")
    list_jobs = []
    for job in jobs :
        processed_job = process_single_job(job)
        if validate_single_job(processed_job) : list_jobs.append(processed_job)
    return list_jobs

def validate_single_job(job,debug=False) :
    """ Returns True if job is valid, False otherwise """
    isOK = True
    if not job['id'].isdigit() :
        isOK = False
        if debug : print("job id not validated")
    if debug and (isOK == False) : print(job)
    return isOK

def process_single_job(job='') :
    """ Returns a dict with a data from single job"""
    job = job.split("\t")
    single_job = { 'id':job[0], 'status':job[1], 'user':job[2], 'script':job[3], 'server':job[4] }
    return single_job

def filter_jobs(jobs,status='',user='vpacik',server='') :
    """ Returns a list with jobs passing filtering criteria """
    filtered_jobs = [ job for job in jobs if job['user'] == user ]
    return filtered_jobs

def get_status(user='vpacik') :
    """
    Fetching jobs from Grid servers, sorting them according to their status
    and prints brief overview
    """
    jobs = get_job_list(get_jobs(str(user)))

    master = []
    master_split = []
    master_done = []
    master_rest = []

    subjobs = []
    subjobs_done = []
    subjobs_running = []
    subjobs_waiting = []
    subjobs_assigned = []
    subjobs_started = []
    subjobs_saving = []
    subjobs_errors = []
    subjobs_rest = []

    print '######################################'
    print '  Jobs status for user "%s"' % user
    for job in jobs:

        if job['server'].startswith("pcapiserv") :
            # masterjob
            master.append(job)

            if job['status'] == 'DONE' : master_done.append(job)
            elif job['status'] == 'SPLIT' : master_split.append(job)
            else : master_rest.append(job)

        elif job['server'].startswith("aliendb") :
            # subjobs
            subjobs.append(job)

            if job['status'] == 'RUNNING' : subjobs_running.append(job)
            elif job['status'] == 'DONE' : subjobs_done.append(job)
            elif job['status'] == 'WAITING' : subjobs_waiting.append(job)
            elif job['status'] == 'ASSIGNED' : subjobs_assigned.append(job)
            elif job['status'] == 'STARTED' : subjobs_started.append(job)
            elif job['status'] == 'SAVING' : subjobs_saving.append(job)
            elif job['status'].startswith('ERROR') : subjobs_errors.append(job)
            else : subjobs_rest.append(job)

        else :
            print('Unknown job server value: '+str(job['server']))



    num_masjob_all = len(master)
    num_masjob_split = len(master_split)
    num_masjob_done = len(master_done)
    num_masjob_rest = len(master_rest)

    num_subjob_all = len(subjobs)
    num_subjob_done = len(subjobs_done)
    num_subjob_run = len(subjobs_running)
    num_subjob_wait = len(subjobs_waiting)
    num_subjob_assign = len(subjobs_assigned)
    num_subjob_start = len(subjobs_started)
    num_subjob_save = len(subjobs_saving)
    num_subjob_error = len(subjobs_errors)
    num_subjob_rest = len(subjobs_rest)


    def printStatusLine(label, num, num_all) :
        perc = -1.0
        if num_all > 0.0 : perc = 100*float(num)/num_all
        print '%10s:  %4d/%d  %5.1f%%' % (label, num, num_all, perc)
        return

    print '======= Masterjobs (%d) ==============' % (num_masjob_all)
    printStatusLine("Done", num_masjob_done, num_masjob_all)
    printStatusLine("Split", num_masjob_split, num_masjob_all)
    printStatusLine("Rest", num_masjob_rest, num_masjob_all)
    print '======= Subjobs (%d) ==============' % (num_subjob_all)
    printStatusLine("Done", num_subjob_done, num_subjob_all)
    printStatusLine("Running", num_subjob_run, num_subjob_all)
    printStatusLine("Waiting", num_subjob_wait, num_subjob_all)
    printStatusLine("Assigned", num_subjob_assign, num_subjob_all)
    printStatusLine("Starting", num_subjob_start, num_subjob_all)
    printStatusLine("Saving", num_subjob_save, num_subjob_all)
    printStatusLine("Rest", num_subjob_rest, num_subjob_all)
    print '######################################'

    #for job in subjobs_rest :
    #    print(job)

    return
# ==============================================================================

use_user = 'vpacik'

get_status(use_user)



# # parsing command-line arguments
# parser = argparse.ArgumentParser(prog='jobs',description="AliGEM module for handling ALICE Grid jobs")
# parser.add_argument("-u", "--user", type=str, default='vpacik', help="Specify a user for the action")
#
# subparsers = parser.add_subparsers(help='')
#
# sub_status = subparsers.add_parser("status", help='Overview of currently registered jobs')
#
# sub_list = subparsers.add_parser("list", help="List of jobs with status")
#
#
#
# sub_kill = subparsers.add_parser("kill", description='Kill a grid job(s)', help='Kill job')
#
#
# args = parser.parse_args()
# args.func(args)
#
# print args
#
# if args.user :
#     use_user = args.user

# if args.status :
        # print get_status(user_conf)
#
