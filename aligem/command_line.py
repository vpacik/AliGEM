import jobs
import argparse
import subprocess

def main() :
    local_user = subprocess.check_output("whoami").strip()
    # print "\n\nYou are logged as '%s'. If this is not your CERN username, please specify -u USER while issuing AliGEM commands" % (local_user)

    ### top-level group (L0)
    parser = argparse.ArgumentParser(description="Welcome to AliGEM - ALICE Grid Enviroment Manager - toolbox for handling Grid related operations.")
    parser.add_argument("-v","--verbose", help="produce verbose output", action="store_true")
    parser.add_argument("-d","--debug", help="debugging mode (additional printout)", action="store_true")
    parser.add_argument("--version", action="version", version='0.1', help="print current version")
    subparsers = parser.add_subparsers(dest="command")

    ### sub-parsers
    # jobs parser (L1)
    parser_jobs = subparsers.add_parser("jobs", help="grid jobs operations")
    jobs_subparsers = parser_jobs.add_subparsers(dest="job_command")

    # jobs sub-parsers (L2)
    jobs_subparser_status = jobs_subparsers.add_parser("status", help = "print overview of currently registered grid jobs")
    # jobs_subparser_status.add_argument("-u","--user", help="specify USER as CERN username")
    jobs_subparser_status.add_argument("-o","--offline", help="running in OFFLINE mode for testing purposes", action="store_true", default=False)
    jobs_subparser_status.add_argument("--only-positive", help="print only states with at least 1 (sub)job", action="store_true", default=False)
    jobs_subparser_status.add_argument("-u","--user", help="specify USER as CERN username", default=local_user)

    jobs_subparser_kill = jobs_subparsers.add_parser("kill", help = "kill grid job(s) in DONE state")
    # jobs_subparser_kill.add_argument("-u","--user", help="specify USER as CERN username")

    jobs_subparser_resubmit = jobs_subparsers.add_parser("resub", help = "re-submit all grid job(s) in ERROR, EXPIRED or ZOMBIE state")

    # token parser (L1)
    # NOTE: not implemented
    parser_token = subparsers.add_parser("token", help="token (not implemented yet)")



    args = parser.parse_args()

    debug = args.debug
    verbose = args.verbose

    if debug :
        print "=== Arguments ================================="
        print args
        print "==============================================="

    if args.command == 'jobs' :
        if debug : print "inside jobs"

        if args.job_command == 'status' :
            if debug : print "inside status"
            offline = args.offline
            only_positive = args.only_positive

            if args.user :
                local_user = args.user
                
            jobs.get_status(local_user,offline=offline, debug=debug, only_positive=only_positive)

        if args.job_command == 'kill' :
            if debug : print "inside kill"
            # user = args.user

            jobs.kill_done(local_user,debug=debug)


        if args.job_command == 'resub' :
            if debug : print "inside resubmit"
            # user = args.user
            jobs.resubmit(local_user,debug=debug)


    if args.command == 'token' :
        print "token command not implemented (yet)"


    return
