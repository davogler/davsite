#!/bin/bash
set -e

LOGFILE=/srv/www/davidalanvogler.com/logs/gunicorn_dav.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
# user/group to run as
USER=admin
GROUP=admin
cd /srv/www/davidalanvogler.com/cms
source /home/admin/envs/davsite/bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec /home/admin/envs/davsite/bin/gunicorn_django -w $NUM_WORKERS -b 0.0.0.0:8000\
  --user=$USER --group=$GROUP --log-level=debug \
  --log-file=$LOGFILE 2>>$LOGFILE