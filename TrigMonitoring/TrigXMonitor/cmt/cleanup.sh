# echo "cleanup TrigXMonitor TrigXMonitor-r502829 in /afs/cern.ch/user/r/rewang/public/cmthome/Trigger/TrigMonitoring"

if test "${CMTROOT}" = ""; then
  CMTROOT=/cvmfs/atlas.cern.ch/repo/sw/software/x86_64-slc6-gcc48-opt/20.3.5/CMT/v1r25p20140131; export CMTROOT
fi
. ${CMTROOT}/mgr/setup.sh
cmtTrigXMonitortempfile=`${CMTROOT}/${CMTBIN}/cmt.exe -quiet build temporary_name`
if test ! $? = 0 ; then cmtTrigXMonitortempfile=/tmp/cmt.$$; fi
${CMTROOT}/${CMTBIN}/cmt.exe cleanup -sh -pack=TrigXMonitor -version=TrigXMonitor-r502829 -path=/afs/cern.ch/user/r/rewang/public/cmthome/Trigger/TrigMonitoring  $* >${cmtTrigXMonitortempfile}
if test $? != 0 ; then
  echo >&2 "${CMTROOT}/${CMTBIN}/cmt.exe cleanup -sh -pack=TrigXMonitor -version=TrigXMonitor-r502829 -path=/afs/cern.ch/user/r/rewang/public/cmthome/Trigger/TrigMonitoring  $* >${cmtTrigXMonitortempfile}"
  cmtcleanupstatus=2
  /bin/rm -f ${cmtTrigXMonitortempfile}
  unset cmtTrigXMonitortempfile
  return $cmtcleanupstatus
fi
cmtcleanupstatus=0
. ${cmtTrigXMonitortempfile}
if test $? != 0 ; then
  cmtcleanupstatus=2
fi
/bin/rm -f ${cmtTrigXMonitortempfile}
unset cmtTrigXMonitortempfile
return $cmtcleanupstatus

