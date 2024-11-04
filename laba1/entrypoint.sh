#!/bin/bash

DIR="csv"
INTERVAL=60
TMP_PATH="/tmp/disk_usage.pid"

init() {
    TIMESTAMP=$(date +%Y%m%d%H%M%S)
    LOGFILE="${DIR}/disk_usage_${TIMESTAMP}.csv"
    mkdir -p "$DIR"
    echo "Timestamp,Filesystem,Size,Used,Avail,Use%,Mounted on" >"$LOGFILE"
}

disk_usage() {
    init

    while true; do
        TIMESTAMP=$(date +%Y-%m-%d\ %H:%M:%S)
        df -h | tail -n +2 | while read -r line; do
            echo "$TIMESTAMP,$line" >>"$LOGFILE"
        done

        if [[ "$(date +%Y%m%d)" != "$(date -r "$LOGFILE" +%Y%m%d)" ]]; then
            init
        fi

        sleep "$INTERVAL"
    done
}

start() {
    disk_usage &
    echo $! >"$TMP_PATH"
    echo "PID $(cat "$TMP_PATH")"
}

stop() {
    if [[ -f $TMP_PATH ]]; then
        PID=$(<$TMP_PATH)
        kill "$PID" && rm "$TMP_PATH"
        echo "Process Stopped"
    else
        echo "Not running"
    fi
}

status() {
    if [[ -f $TMP_PATH ]]; then
        PID=$(<$TMP_PATH)
        if ps -p "$PID" >/dev/null; then
            echo "PID $PID"
            return
        fi
    fi
    echo "Not running"
}

case "$1" in
START)
    start
    ;;
STOP)
    stop
    ;;
STATUS)
    status
    ;;
*)
    echo "Params: START|STOP|STATUS"
    exit 1
    ;;
esac
