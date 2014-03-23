from fabric.api import task
from fabric.context_managers import cd, prefix
from fabric.operations import run
from fabric.contrib.files import exists

github_repo_url = "https://github.com/cgibson/blog"

pelican_virtualenv = "~/env/pelican"

remote_repo_dir = "~/Projects/blog"

remote_beta_dir = "/sites/mrvoxel/beta"
remote_beta_redir_file = "/sites/mrvoxel/site-map-beta.lua"

remote_publish_dir = "/sites/mrvoxel/www"
remote_publish_redir_file = "/sites/mrvoxel/site-map.lua"

def title(text):
    print "=" * 80
    print " " + str(text)
    print "=" * 80

@task
def deploy():
    deploy_to(beta=True)

@task
def deploy_prod():
    deploy_to(beta=False)

def deploy_to(beta=True):   
    title("Deploying to %s server." % ("beta" if beta else "prod")

    output_dir = remote_beta_dir if beta else remote_publish_dir
    redir_file = remote_beta_redir_file if beta else remote_publish_redir_file

    if not exists(remote_repo_dir):
        print "Repo dir doesn't exist. Building."
        run("mkdir -p %s" % remote_repo_dir)
        run("git clone %s %s" % (github_repo_url, remote_repo_dir))

    with cd(remote_repo_dir):
        run("git pull")

        run("git submodule update --init --recursive")
        with cd("theme"):
            run("git checkout master")
            run("git pull")


        # Now build the site
        with prefix("source %s/bin/activate" % pelican_virtualenv):
            run("make publish")

        # Copy generated files to their respective spots
        run("cp -r %s/output %s" % (remote_repo_dir, output_dir))
        run("cp %s/output/site-map.lua %s" % (remote_repo_dir, redir_file))
