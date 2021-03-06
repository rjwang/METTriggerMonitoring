#!/usr/bin/env python

###########################################################################
#
# The convention in this file is to NOT capitalize the functions.
#
# def findIdx()
# def getQUERY_STRING()
# def linkDataSummary()
# def linkRunQuery()
# def linkTrigConf()
# def linkRunSummary()
# def printIncludes()
# def printHeader()
# def printRuns()
# def printButtons()
# def printCuts()
# def printDownload()
# def printAllcharts()
# def printChartOnly()
# def printOnechart()
# def printCustomize()
# def printTriggers()
# def printRadioOption()
# def printRunranges()
# def printAbout()
# def printTutorial()
# def printFooter()
# def test()
#
###########################################################################

import cgi
import datetime
import TrigXMonitor.xmonHtmlUtility as xhu
import TrigXMonitor.xmonListUtility as xlu

fontface = 'Arial' #'Arial Narrow'
comingsoon = '<span class="sc" style="color:red;">Soon</span>'
author = 'Tae Min Hong'
author2 = 'Elliot Lipeles'
updatefreq  = 20

link = dict()
link['site']            = 'https://rewang.web.cern.ch/rewang/xmon'
link['author']          = 'http://consult.cern.ch/xwho/people/538626'
link['author2']         = 'http://consult.cern.ch/xwho/people/662221'
link['outreach']        = "http://www.slac.stanford.edu/~thong/outreach/"
link['TrigXMonitor']    = 'https://svnweb.cern.ch/trac/atlasoff/browser/Trigger/TrigMonitoring/TrigXMonitor/trunk'
link['TrigCostPython']  = 'https://svnweb.cern.ch/trac/atlasoff/browser/Trigger/TrigCost/TrigCostPython/trunk'
link['logout']          = 'https://login.cern.ch/adfs/ls/?wa=wsignout1.0'
link['makeRoot.py']     = 'https://svnweb.cern.ch/trac/atlasoff/browser/Trigger/TrigCost/TrigCostPython/trunk/macros/makeRoot.py'
link['exampleCost.py']  = 'https://svnweb.cern.ch/trac/atlasoff/browser/Trigger/TrigCost/TrigCostPython/trunk/macros/exampleCost.py'
link['xmon.cgi']        = 'https://svnweb.cern.ch/trac/atlasoff/browser/Trigger/TrigMonitoring/TrigXMonitor/trunk/macros/xmon.cgi'
link['includes.html']   = '%s/html/includes.html'   % link['site']
link['header.html']     = '%s/html/header.html'     % link['site']
link['body.html']       = '%s/html/body.html'       % link['site']
link['footer.html']     = '%s/html/footer.html'     % link['site']
link['acrontablist']    = 'https://svnweb.cern.ch/trac/atlasoff/browser/Trigger/TrigCost/TrigCostPython/trunk/macros/acrontablist.txt'
link['COOL']            = 'https://twiki.cern.ch/twiki/bin/viewauth/Atlas/CoolOnlineData'
link['TRP']             = 'https://twiki.cern.ch/twiki/bin/view/Atlas/TRPInfo'
link['DataSummary']     = 'https://atlas.web.cern.ch/Atlas/GROUPS/DATAPREPARATION/DataSummary'
#link['DB']              = 'https://cern.ch/x/root/?C=M;O=D'
link['DB']              = 'https://rewang.web.cern.ch/rewang/xmon/root/?C=M;O=D'
trig_to_restId = "document.getElementById('trigId'),document.getElementById('restId')"
rest_to_trigId = "document.getElementById('restId'),document.getElementById('trigId')"

#==========================================================================
def findIdx(runlist, alllist):
    idxlist = []
    for run in runlist:
        for idx, i in enumerate(alllist):
            if run==i:
                idxlist.append(idx)

    return idxlist


#==========================================================================
def getQUERY_STRING(omitlist=[]):

    fields = cgi.FieldStorage()
    QUERY_STRING = link['site'] + '/cgi-bin/xmon.cgi?q='
    for i, item in enumerate(fields.value):
        if item.name in omitlist:
            continue
        QUERY_STRING += '&%s=%s' % (item.name, item.value)

    return QUERY_STRING


#==========================================================================
def linkDataSummary(run):
    year = 2016
    if   run <= 142402: year = 2009
    elif run <= 168726: year = 2010
    return '%s/%d/run.py?run=%d' % (link['DataSummary'], year, run)


#==========================================================================
def linkRunQuery(run):
    return 'https://atlas-runquery.cern.ch/query.py?q=find+run+%d+and+ready+%%2F+show+all' % run




#==========================================================================
def linkTrigConf(run):
    return 'https://atlas-trigconf.cern.ch/listruns/?runs=%d' % run


#==========================================================================
def linkRunSummary(run):
    return 'http://cern.ch/atlas-service-db-runlist/cgi-bin/runDetails.py?run=%d' % run


#==========================================================================
def printIncludes(tab='', site=link['site'], virtual=''):

    if len(virtual)>0:
        return xhu.Print(tab, '<!--#include virtual="%s" -->' % virtual)

    begintab = tab
    tab = xhu.Print(tab, '<!-- BEGIN Includes (tab=%d) -->' % len(begintab) )
    tab = xhu.Print(tab, '<title>ATLAS MET XMonitor</title>')
    tab = xhu.Print(tab, '<meta name="ATLAS_XMonitor" content="ATLAS MET XMonitor"/> ')
    tab = xhu.Print(tab, '<meta http-equiv="pragma" content="no-cache;text/html;charset=ISO-8859-1"/>')
#	    tab = xhu.Print(tab, '<meta http-equiv="refresh" content="600"/>')

    #
    # External scripts & styles must come first
    #

    # Jquery
    #tab = xhu.Print(tab, '<script src="%s/css/jquery.min.js" type="text/javascript"></script>' % site)
    tab = xhu.Print(tab, '<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>')

    # Highcharts
    #tab = xhu.Print(tab, '<script src="%s/css/highcharts/js/highcharts.js" type="text/javascript"></script>' % site)
    #tab = xhu.Print(tab, '<script src="%s/css/highcharts/js/modules/exporting.src.js" type="text/javascript"></script>' % site)
    tab = xhu.Print(tab, '<script src="%s/css/Highcharts-4.2.5/js/highcharts.js" type="text/javascript"></script>' % site)
    tab = xhu.Print(tab, '<script src="%s/css/Highcharts-4.2.5/js/modules/exporting.src.js" type="text/javascript"></script>' % site)


    # Highslide
    #tab = xhu.Print(tab, '<script src="%s/css/highslide/highslide-with-gallery.js" type="text/javascript"></script>' % site)
    #tab = xhu.Print(tab, '<link  href="%s/css/highslide/highslide.css" type="text/css" rel="stylesheet"/>' % site)

    tab = xhu.Print(tab, '<script src="%s/css/highslide-5.0.0/highslide/highslide-with-gallery.js" type="text/javascript"></script>' % site)
    tab = xhu.Print(tab, '<link  href="%s/css/highslide-5.0.0/highslide/highslide.css" type="text/css" rel="stylesheet"/>' % site)



    # Tabber
    tab = xhu.Print(tab, '<script src="%s/css/tabber.js" type="text/javascript"></script>' % site)
    tab = xhu.Print(tab, '<style type="text/css">.tabber{display:none;}</style>')

    # Dropdownmenu
    tab = xhu.Print(tab, '<script src="%s/css/menucontents.js" type="text/javascript"></script>' % site)
    tab = xhu.Print(tab, '<script src="%s/css/anylinkmenu.js" type="text/javascript"></script>' % site)
    tab = xhu.Print(tab, '<script type="text/javascript">anylinkmenu.init("menuanchorclass");</script>')

    # Dropdownmenu -- click for runs
    tab = xhu.Print(tab, '<script src="%s/css/simple.js" type="text/javascript"></script>' % site)

    # List table & submit all
    tab = xhu.Print(tab, '<script src="%s/css/autoselect.js" type="text/javascript"></script>' % site)

    # Regex
    tab = xhu.Print(tab, '<script src="%s/css/filterlist.js" type="text/javascript"></script>' % site)

    # Clear default input
    tab = xhu.Print(tab, '<script src="%s/css/util-functions.js" type="text/javascript"></script>' % site)
    tab = xhu.Print(tab, '<script src="%s/css/clear-default-text.js" type="text/javascript"></script>' % site)

    #
    # Local script & styles must come after external ones above
    #

    tab = xhu.Print(tab, '<link  href="%s/images/atlas.ico" rel="shortcut icon"/> ' % site)
    tab = xhu.Print(tab, '<link  href="%s/css/xmon.css" type="text/css" rel="stylesheet"/>' % site)

    tab = xhu.Print(tab, '<!-- END Includes (tab=%d begintab=%d same=%s) -->' % (len(tab), len(begintab), 'YES' if len(tab)==len(begintab) else 'NO') )

    return tab


#==========================================================================
def printHeader(tab='', site=link['site'], virtual='', xmonParams=None):

    if len(virtual)>0:
        return xhu.Print(tab, '<!--#include virtual="%s" -->' % virtual)

    begintab = tab
    tab = xhu.Print(tab, '<!-- BEGIN Header (tab=%d) -->' % len(begintab) )

    # Top table
    tab = xhu.Print(tab, '<table class="toptable" style="height:100px;">')

    # New row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td colspan=3 style="text-align:right; margin-right:4px; padding-right:4px;">')
    tab = printRuns(tab, xmonParams)
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '<h1>ATLAS MET Trigger Rate/Cross-section Monitor</h1>')
    tab = xhu.Print(tab, '</tr>')

    # New row
    tab = xhu.Print(tab, '<tr style="vertical-align:top; text-align:right;"> ')
    # Item
    tab = xhu.Print(tab, '<td style="width:90px;"></td>')
    tab = xhu.Print(tab, '<td rowspan=2>')
#	    tab = xhu.Print(tab, '<a href="%s/cgi-bin/xmon.cgi" style="border-bottom:0px;">' % site)
#	    tab = xhu.Print(tab, '<a href="%s/html/default.html" style="border-bottom:0px;">' % site)
    tab = xhu.Print(tab, '<a class="menuanchorclass" rel="title" style="border-bottom:0px;">')
    #tab = xhu.Print(tab, '<img src="%s/images/title.gif" style="width:375px;"/>' % site)
#    tab = xhu.Print(tab, '<img src="%s/images/ATLAS-Logo.png" style="width:115px;"/>' % site)
    tab = xhu.Print(tab, '</a>')
    tab = xhu.Print(tab, '</td>')

    # Item
    tab = xhu.Print(tab, '<td style="text-align:right;">')
    tab = printButtons(tab, xmonParams)
    tab = xhu.Print(tab, '</td>')

    # Close row
    tab = xhu.Print(tab, '</tr>')

    # New row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td colspan=3 style="text-align:right; margin-right:4px; padding-right:4px;">')
#    tab = xhu.Print(tab, '<font style="color:white;">&bull;</font>')
#    tab = xhu.Print(tab, '<a style="color:yellow;" class="menuanchorclass" rel="runlist[click]" title="Click to reveal list">Special run list</a>')
#    tab = xhu.Print(tab, '<font style="color:white;">&bull;</font> ')
#    tab = xhu.Print(tab, '<a style="color:yellow;" class="menuanchorclass" rel="availtrigs[click]" title="Click to reveal list">Pre-defined trigger groups</a>')

    #RJ
#    tab = xhu.Print(tab, '<font style="color:red;">&bull;</font>')
#    tab = xhu.Print(tab, '<font face="%s">AUTO RUNS:</font>' % fontface)
#    tab = xhu.Print(tab, '<form style="display:inline;" name="runForm" method="get" action="%s/cgi-bin/xmon.cgi">' % link['site'])
#
    # RJ
    # Add AUTO RUNS Button
#    tab = xhu.Print(tab, '<font style="color:red;">&bull;</font>')
#    qstring = getQUERY_STRING('autorun')
#    tab = xhu.Print(tab, '<a class="whitelink" href="%s&autorun=1">AUTORUN</a>' % (qstring))


    tab = xhu.Print(tab, '</form>')

    #RJ
    tab = xhu.Print(tab, '<font style="color:red;">&bull;</font>')
    tab = xhu.Print(tab, '<font face="%s">NUM OF RUNS TO SHOW:</font>' % fontface)
    tab = xhu.Print(tab, '<form style="display:inline;" name="runForm" method="get" action="%s/cgi-bin/xmon.cgi">' % link['site'])
    tab = xhu.Print(tab, '<input name="nrun" type="text" size="2" style="color:black;" value="%s" class="cleardefault"></input>' % '3' ) #runstring + 'etc.')
    tab = xhu.Print(tab, ' < 30')
    tab = xhu.Print(tab, '</form>')




    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '</tr>')


    # Close table
    tab = xhu.Print(tab, '</table>')

#	    import sys
#	    sys.exit()

    tab = xhu.Print(tab, '<!-- END Header (tab=%d begintab=%d same=%s) -->' % (len(tab), len(begintab), 'YES' if len(tab)==len(begintab) else 'NO') )

    return tab


#==========================================================================
def printRuns(tab = '', xmonParams=None):

    # Recent run list
    tab = xhu.Print(tab, '<font style="color:yellow;">&bull;</font>')
    tab = xhu.Print(tab, '<font face="%s">RECENT RUNS:</font>' %fontface) # % xlu.readLastNrun()[0])
    lastrun = xlu.readLastRun(xmonParams.inputs['ntup'])
    tab = xhu.OpenMenu(tab, 'menu')
    for i in lastrun[:xmonParams.inputs['lastrunlist']]:
        i.replace(' ','')
        run = xmonParams.inputs['run']
        thisrun = i in run
        i = int(i)
        qstring = getQUERY_STRING('run')
        linkXmon = '%s&run=%d' % (qstring, i)
        qstring = getQUERY_STRING('mode')
        linkCompare = '%s&run=%d&mode=compare' % (qstring, i)
        tab = xhu.PrintMenuRun(tab, i, thisrun,
                               linkXmon,
                               linkCompare,
                               linkDataSummary(i),
                               linkRunQuery(i),
                               linkTrigConf(i),
                               linkRunSummary(i),
                               'menu')

#	        if i in run:
#	            tab = xhu.Print(tab, '<a class="selected">%s</a>' % str(i))
#	        else:
#	            qstring = getQUERY_STRING('run')
#	            tab = xhu.Print(tab, '<a class="whitelink" href="%s&run=%s">%s</a>' % (qstring, str(i), str(i)))

    tab = xhu.CloseMenu(tab)

    # Input box
    runstring = ''
    if   len(lastrun)>7: runstring = str(lastrun[6])+','+str(lastrun[7])
    if   len(lastrun)>6: runstring = str(lastrun[5])+','+str(lastrun[6])
    elif len(lastrun)>5: runstring = str(lastrun[4])+','+str(lastrun[5])
    elif len(lastrun)>4: runstring = str(lastrun[3])+','+str(lastrun[4])
    elif len(lastrun)>3: runstring = str(lastrun[2])+','+str(lastrun[3])
    elif len(lastrun)>2: runstring = str(lastrun[1])+','+str(lastrun[2])
    elif len(lastrun)>1: runstring = str(lastrun[0])+','+str(lastrun[1])
    elif len(lastrun)>0: runstring = str(lastrun[0])

    tab = xhu.Print(tab, '<form style="display:inline;" name="runForm" method="get" action="%s/cgi-bin/xmon.cgi">' % link['site'])
    tab = xhu.Print(tab, '<input name="run" type="text" size="11" style="color:black;" value="%s" class="cleardefault"></input>' % 'put run here' ) #runstring + 'etc.')
    tab = xhu.Print(tab, '</form>')

#	    # General run button
#	    tab = xhu.OpenMenu(tab, 'menu')
#	#	    tab = xhu.Print(tab, '<li class="sub">')
#	#	    tab = xhu.Print(tab, '<a onmouseout="unclickMenu(%s);" onmouseover="clickMenu(%s);">runs</a>' % ("'menu'", "'menu'"))
#	#	    tab = xhu.Print(tab, '<ul>')
#	#	    tab = xhu.Print(tab, '<li>Run list</li>'
#	#	    tab = xhu.Print(tab, '</ul>')
#	#	    tab = xhu.Print(tab, '</li>')
#	    for idx, year in enumerate(yearlist):
#	        runyearlist = sorted(availruns[year], reverse=True)
#	        for jdx, i in enumerate(runyearlist):
#	            thisrun = (i in runlist)
#	            qstring = getQUERY_STRING('run')
#	            linkXmon = '%s&run=%d' % (qstring, i)
#	            qstring = getQUERY_STRING('mode')
#	            linkCompare = '%s&run=%d&mode=compare' % (qstring, i)
#	            tab = xhu.PrintMenuRun(tab, i, thisrun,
#	                                   linkXmon,
#	                                   linkCompare,
#	                                   linkDataSummary(i),
#	                                   linkRunQuery(i),
#	                                   linkTrigConf(i),
#	                                   linkRunSummary(i),
#	                                   'menu')
#	    tab = xhu.CloseMenu(tab)

    return tab

#==========================================================================
def printButtons(tab = '', xmonParams=None):

    #
    # User data
    #

    runlist = xmonParams.inputs['runlist']
    availlb = ['auto', '1', '2', '4', '6', '8', ]
    thisyear = 2011
    availruns = {2010: [167680, ],
                 2011: [177531, 177539, 177540, 177593, 177682, ],
                }
    yearlist = sorted(availruns.keys(), reverse=True)
    npadding = 0 if len(runlist) > 1 else 1 # nruns shown around those in our list
    psdict = {}
    pskeys = []
    xhu.AppendEntry(psdict, pskeys, 'bp', 'input')
    xhu.AppendEntry(psdict, pskeys, 'ap', 'after-prescale')
    xhu.AppendEntry(psdict, pskeys, 'av', 'output')
    pagedict = {}
    pagekeys = []
    xhu.AppendEntry(pagedict, pagekeys, 'full',     'default')
    xhu.AppendEntry(pagedict, pagekeys, 'chart',    'onepage')
    #xhu.AppendEntry(pagedict, pagekeys, 'png',      'png')
    #xhu.AppendEntry(pagedict, pagekeys, 'pdf',      'pdf')
    modedict = {}
    modekeys = []
    xhu.AppendEntry(modedict, modekeys, 'compare',  'runs &amp; trig')
    xhu.AppendEntry(modedict, modekeys, 'merge',    'trig only')

    #
    # Begin module
    #

    # Open table
    begintab = tab
    tab = xhu.Print(tab, '<!-- BEGIN Buttons (tab=%d)-->' % len(begintab))
    tab = xhu.Print(tab, '<table style="width:100%; color:white; font-size:11pt; padding:0; margin:0">')

    # New row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td style="text-align:right;">')

    # Put cool/trp button
    tab = xhu.Print(tab, '<font style="color:yellow;">&bull;</font>')
    tab = xhu.Print(tab, '<font face="%s">DB:</font>' % fontface)
    for idx, i in enumerate(['cool', 'trp']):
        ntup = xmonParams.inputs['ntup']
        thisntup = ntup == i
        if thisntup:
            tab = xhu.Print(tab, '<a class="selected">%s</a>' % i)
        else:
            qstring = getQUERY_STRING('ntup')
            tab = xhu.Print(tab, '<a class="whitelink" href="%s&ntup=%s">%s</a>' % (qstring, i, i))

    # Put page button
    tab = xhu.Print(tab, '<font style="color:yellow;">&bull;</font> ')
    tab = xhu.Print(tab, '<font face="%s">PAGE STYLE:</font>' % fontface)
    for i in pagekeys:
        page = xmonParams.inputs['page']
        thispage = int( i == page )
        if thispage:
            tab = xhu.Print(tab, '<a class="selected">%s</a> ' % pagedict[i])
        else:
            if   i=='png': tab = xhu.Print(tab, '%s' % (pagedict[i]))
            elif i=='pdf': tab = xhu.Print(tab, '%s' % (pagedict[i]))
            else:
            	qstring = getQUERY_STRING('page')
            	tab = xhu.Print(tab, '<a class="whitelink" href="%s&page=%s">%s</a>' % (qstring, i, pagedict[i]))

    # Input box
    tab = xhu.Print(tab, '<font style="color:yellow;">&bull;</font>')
    tab = xhu.Print(tab, '<font face="%s">TRIGS:</font>' % fontface)
    tab = xhu.Print(tab, '<form style="display:inline;" name="trigForm" method="get" action="%s/cgi-bin/xmon.cgi">' % link['site'])
    tab = xhu.Print(tab, '<input name="trig" type="text" size="11" style="color:black;" value="put trig here" class="cleardefault"></input>')
    tab = xhu.Print(tab, '</form>')


    # New row
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '</tr>')
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td style="text-align:right;">')

#	    # Put lumi=0 suppression button
#	    tab = xhu.Print(tab, '<font style="color:yellow;">&bull;</font>')
#	    tab = xhu.Print(tab, '<font face="%s">X-AXIS:</font>' % fontface)
#	    for idx, i in enumerate(['no cut', 'L/bunch&gt;e27']):
#	        xcut = xmonParams.inputs['xcut']
#	        thisxcut = int(('log' in i and xcut=='1') or ('log' not in i and xcut=='0'))
#	        if thisxcut:
#	            tab = xhu.Print(tab, '<a class="selected">%s</a>' % i)
#	        else:
#	            qstring = getQUERY_STRING('xcut')
#	            tab = xhu.Print(tab, '<a class="whitelink" href="%s&xcut=%d">%s</a>' % (qstring, idx, i))

    # Put log/linear button
    tab = xhu.Print(tab, '<font style="color:yellow;">&bull;</font>')
    tab = xhu.Print(tab, '<font face="%s">Y-AXIS:</font>' % fontface)
    for idx, i in enumerate(['linear', 'log']):
        logy = xmonParams.inputs['logy']
        thislogy = int(('log' in i and logy=='1') or ('log' not in i and logy=='0'))
        if thislogy:
            tab = xhu.Print(tab, '<a class="selected">%s</a>' % i)
        else:
            qstring = getQUERY_STRING('logy')
            tab = xhu.Print(tab, '<a class="whitelink" href="%s&logy=%d">%s</a>' % (qstring, idx, i))

    # Put grid button
    tab = xhu.Print(tab, '<font style="color:yellow;">&bull;</font>')
    tab = xhu.Print(tab, '<font face="%s">GRID:</font>' % fontface)
    for i in ['no', 'x', 'y', 'xy']:
        grid = xmonParams.inputs['grid']
        thisgrid = i==grid if i!='no' else (i in grid)
        if thisgrid:
            tab = xhu.Print(tab, '<a class="selected">%s</a> ' % i)
        else:
            qstring = getQUERY_STRING('grid')
            tab = xhu.Print(tab, '<a class="whitelink" href="%s&grid=%s">%s</a>' % (qstring, i, i))

    # Put lbsample button
    tab = xhu.Print(tab, '<font style="color:yellow;">&bull;</font>')
    tab = xhu.Print(tab, '<font face="%s">LB SAMPLING:</font>' % fontface)
    for idx, i in enumerate(availlb):
        lbsample = xmonParams.inputs['lbsample']
        thislb = False
        if lbsample=='auto':
            if len(runlist)>4:
                thislb = i=='8'
            else:
                thislb = (i==lbsample) or (i==str(2*len(runlist)))
        if thislb:
            tab = xhu.Print(tab, '<a class="selected">%s</a>' % i)
        else:
            qstring = getQUERY_STRING('lbsample')
            tab = xhu.Print(tab, '<a class="whitelink" href="%s&lbsample=%s">%s</a>'
                            % (qstring, i, i))

    # Input box
    tab = xhu.Print(tab, '<form style="display:inline;" name="lbForm" method="get" action="%s/cgi-bin/xmon.cgi">' % link['site'])
    tab = xhu.Print(tab, '<input name="lbsample" type="text" size="3" style="color:black;" value="10" class="cleardefault"></input>')
    tab = xhu.Print(tab, '</form>')

    # New row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td style="text-align:right;">')

    # Put bp/ap/av button
    tab = xhu.Print(tab, '<font style="color:yellow;">&bull;</font>')
    tab = xhu.Print(tab, '<font face="%s">RATES &amp; X-SEC:</font>' % fontface)
    for i in pskeys:
        ps = xmonParams.inputs['ps']
        thislb = (i==ps)
        if thislb:
            tab = xhu.Print(tab, '<a class="selected">%s</a> ' % psdict[i])
        else:
            qstring = getQUERY_STRING('ps')
            tab = xhu.Print(tab, '<a class="whitelink" href="%s&ps=%s">%s</a>'
                            % (qstring, i, psdict[i].replace('prescaling','ps')))

    # Put compare button
    tab = xhu.Print(tab, '<font style="color:yellow;">&bull;</font>')
    tab = xhu.Print(tab, '<font face="%s">COMPARE:</font>' % fontface)
    for i in modekeys:
        mode = xmonParams.inputs['mode']
        thismode = i in mode
        if thismode:
            tab = xhu.Print(tab, '<a class="selected">%s</a>' % modedict[i])
        else:
            qstring = getQUERY_STRING('mode')
            tab = xhu.Print(tab, '<a class="whitelink" href="%s&mode=%s">%s</a>' % (qstring, i, modedict[i]))


    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '</tr>')



    # Close table
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '</tr>')
    tab = xhu.Print(tab, '</table>')
    tab = xhu.Print(tab, '<!-- END Buttons (tab=%d begintab=%d same=%s) -->' % (len(tab), len(begintab), 'YES' if len(tab)==len(begintab) else 'NO') )

#	    # New line
#	    tab = xhu.Print(tab, '<br/>')
#
#	    menuname = 'menu'
#
#
#	    tab = xhu.Print(tab, '<br/>')
#	    #
#	    #
#	    #
#	    # Put trigger button
#	    #
#	    #
#	    #
#	    availtrigs = {
#	        'Pre-defined trigger groups':
#	        {
#	            'Mixed minbias'     : 'L1_ZDC L1_LUCID L1_MBTS_1_1 L1_MBTS_4_4 EF_mbSpTrk EF_mbZdc_eff EF_mbLucid_eff',
#	            'EF muons'          : 'EF_mu13 EF_mu13_MG EF_mu20 EF_2mu6 EF_2mu4_Jpsimumu EF_2mu10_loose',
#	            'EF electrons'      : 'EF_e10_medium EF_e15_medium EF_e20_loose EF_g20_loose EF_2e10_medium',
#	            'EF jets'           : 'EF_L1J175_NoAlg EF_L1J250_NoAlg',
#	            'EF Met'            : 'EF_xe30_noMu EF_xe40_noMu EF_xe80_noMu EF_te900',
#	            'Mixed muons'       : 'EF_mu20 L2_mu20 L1_MU10',
#	            'Higher mixed elec' : 'EF_e15_medium L2_e15_medium L1_EM10',
#	            'Lower mixed elec'  : 'EF_e10_medium L2_e10_medium L1_EM5',
#	            'Mixed jets'        : 'EF_L1J175_NoAlg L2_L1J175_NoAlg L1_J175',
#	            'Mixed Met'         : 'EF_xe80_noMu L2_xe60_noMu L1_XE60',
#	            'Lowest unprescaled': 'EF_e15_tight EF_mu20 EF_L1J175_NoAlg EF_xe80_noMu EF_te600 EF_tau125_medium',
#	        },
#	    }
#
#	    triglist = xmonParams.inputs['varlist']
#
#	    # Indiv trigger buttons
#	    for trig in availtrigs.keys():
#	        qstring, first = getQUERY_STRING('trig')
#	        linkXmon = '%s%strig=' % (qstring, '?' if first else '&')
#	        tab = xhu.PrintMenuTrig(tab, trig, availtrigs[trig], linkXmon, menuname)


    return tab


#==========================================================================
# Print cuts
#
# Defined in xmonInputsHandler::readInput()
# Coordinate with xmonDataObject::cutVar()
#
def printCuts(tab = '', xmonParams=None):

    tab = xhu.Print(tab, '<div style="text-align:left;">')
    tab = xhu.Print(tab, '<b>Data selection criteria</b><br/>')

    cutlist = ['lblength', 'lumi', 'bunchlumi', 'mu', 'bunches'] # Basic cuts
    cutlist += ['L1_XE50'] # Add trigger-based cuts

    for var in cutlist:
        cut = ''
        isunit = False

        # If trigger, change label
        istrig = var.split('_')[0] in ['L1','L2','EF']
        if istrig: varlabel = 'trig'
        else:      varlabel = var

        # Impose minimum if set
        if xmonParams.inputs[var+'min'] > -1:
            cut += '%g ' % xmonParams.inputs[var+'min']
            if xmonParams.inputs[var+'max'] == -1:
                cut += ' %s' % xmonParams.niceLabelUnit[varlabel]
                isunit = True

            cut += ' &lt;&nbsp;'

        # Put unit label
        if istrig:
            cut += ' %s' % var
        else:
            cut += xmonParams.niceLabelAbbr[varlabel]

        # Impose maximum if set
        if xmonParams.inputs[var+'max'] > -1:
            cut += '&nbsp;&lt; %g' % xmonParams.inputs[var+'max']

        # Put unit label (only once though)
        if not isunit:
            if istrig:
                cut += ' %s' % var
            else:
                cut += ' %s' % xmonParams.niceLabelUnit[varlabel]

        tab = xhu.Print(tab, cut+'<br/>')

    tab = xhu.Print(tab, '</div>')
    return tab


#==========================================================================
# Put ROOT download link here
#
def printDownload(tab = '', xmonParams=None):

    triglist = xmonParams.inputs['evtlist']['trig']
    isout = xmonParams.inputs['ntup']=='cool' and xmonParams.inputs['ps']=='av'
    isef  = 'EF__' in ' '.join(triglist)
    isl2  = 'L2__' in ' '.join(triglist)
    ishlt = isef or isl2
    if isout and ishlt:
            tab = xhu.Print(tab, '<div style="text-align:middle; color:red;">')
            tab = xhu.Print(tab, 'Caveat emptor: COOL problems with HLT rates &rarr; try the TRP option.')
            tab = xhu.Print(tab, '</div>')

    tab = xhu.Print(tab, '<div style="text-align:right;">')
    tab = xhu.Print(tab, '<a class="menuanchorclass" rel="download[click]" title="Click to reveal list">Download ntuple</a>')
    tab = xhu.Print(tab, '</div>')
    return tab


#==========================================================================
def printAllcharts(tab = '', xmonParams=None, xmonData=None, page=''):

    chartbasewidth = 800

    begintab = tab
    tab = xhu.Print(tab, '<!-- BEGIN All charts (tab=%d) -->' % len(begintab) )

    # Y-type variables = ['x', 'r'] for x-section, rates
    for yChartIdx in xrange( len(xmonParams.yVarList) ):

        # Only show desired mode
        yVarName = xmonParams.yVarList[yChartIdx]
        psName   = xmonParams.inputs['ps']
        yLabel   = xmonParams.niceLabel[ 'tab_' + yVarName ]

#	        # Skip cross-section plots for after-veto counts
#	        if yVarName=='x' and psName=='av':
#	            continue

        # Open tab -- put buttons between the two tab groups
        tab = xhu.Print(tab, '<div class="tabbertab" title="%s" style="width:%dpx;">' % ( yLabel.capitalize(), chartbasewidth+75 ))
        #tab = printDownload(tab, xmonParams)
        tab = xhu.Print(tab, '<div class="tabber">')

        # X-axis variable = 'time', 'lumi'
        for xChartIdx, xVarName in enumerate(xmonParams.xVarList):

            # Name
            chartIdx = [xChartIdx, yChartIdx]
            xVarName = xmonData.getChartName( chartIdx, 'x' )
            xLabel = xmonParams.niceLabel[ 'tab_' + xVarName ]

            # Open tab
            begintab2 = tab
            tab = xhu.Print(tab, '<!-- BEGIN One chart with (tab=%d) -->' % len(begintab2) )
            tab = xhu.Print(tab, '<div class="tabbertab" title="%s" style="width:%dpx;">' % (xLabel, chartbasewidth+65))

            # Layout one chart
            tab = printOnechart( tab, xmonParams, xmonData.getChartNumber(chartIdx) )

            # Close tab
            tab = xhu.Print(tab, '</div>')
            tab = xhu.Print(tab, '<!-- END One chart %s (tab=%d begintab=%d same=%s) -->' % (xLabel, len(tab), len(begintab2), 'YES' if len(tab)==len(begintab2) else 'NO') )

        # Close tab
        tab = xhu.Print(tab, '</div>')
        tab = printCuts(tab, xmonParams)
        tab = xhu.Print(tab, '</div>')
        tab = xhu.Print(tab, '<!-- %s -->' % (yLabel.capitalize()))

    tab = xhu.Print(tab, '<!-- END All chart (tab=%d begintab=%d same=%s) -->' % (len(tab), len(begintab), 'YES' if len(tab)==len(begintab) else 'NO') )
    return tab


#==========================================================================
def printChartOnly(tab='', site=link['site'], xmonParams=None):

    tab = xhu.Print(tab, '<head>')
    tab = xhu.Print(tab, '<script src="%s/css/jquery.min.js" type="text/javascript"></script>' % site)
#    tab = xhu.Print(tab, '<script src="%s/css/highcharts/js/highcharts.js" type="text/javascript"></script>' % site)
#    tab = xhu.Print(tab, '<script src="%s/css/highcharts/js/modules/exporting.src.js" type="text/javascript"></script>' % site)
    tab = xhu.Print(tab, '<script src="%s/css/Highcharts-4.2.5/js/highcharts.js" type="text/javascript"></script>' % site)
    tab = xhu.Print(tab, '<script src="%s/css/Highcharts-4.2.5/js/modules/exporting.src.js" type="text/javascript"></script>' % site)


    tab = xhu.Print(tab, '<script src="%s/css/rgbcolor.js" type="text/javascript" ></script>' % site)
#	    tab = xhu.Print(tab, '<script src="%s/css/canvg.js" type="text/javascript" ></script>' % site)
#	    tab = xhu.Print(tab, '<script src="%s/css/base64.js" type="text/javascript"></script>' % site)
#	    tab = xhu.Print(tab, '<script src="%s/css/canvas2image.js" type="text/javascript"></script>' % site)
#	    tab = xhu.Print(tab, '<script src="%s/css/save.js" type="text/javascript"></script>' % site)
    tab = xhu.Print(tab, '</head>')

    # Body
    tab = xhu.Print(tab, '<body>')
    plotstyle = 'width:%dpx; height:%dpx;' % ( xmonParams.inputs['width'], xmonParams.inputs['height'] )
    tab = xhu.Print(tab, '<body>')
    tab = xhu.Print(tab, '<table border=1>')
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td><div id="xmonChart%d" style="%s"></div></td>' % ( 11, plotstyle ))
    tab = xhu.Print(tab, '<td><div id="xmonChart%d" style="%s"></div></td>' % ( 21, plotstyle ))
    tab = xhu.Print(tab, '<td><div id="xmonChart%d" style="%s"></div></td>' % ( 31, plotstyle )) #RJ
    tab = xhu.Print(tab, '</tr>')
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td><div id="xmonChart%d" style="%s"></div></td>' % ( 12, plotstyle ))
    tab = xhu.Print(tab, '<td><div id="xmonChart%d" style="%s"></div></td>' % ( 22, plotstyle ))
    tab = xhu.Print(tab, '<td><div id="xmonChart%d" style="%s"></div></td>' % ( 32, plotstyle )) #RJ
    tab = xhu.Print(tab, '</tr>')
    tab = xhu.Print(tab, '</table>')
    tab = xhu.Print(tab, '</body>')

    return tab


#==========================================================================
# Used by tabOnechart()
# Uses None
#
def printOnechart(tab='', xmonParams=None, chartNumber=0, page=''):

    # Size & style
    plotstyle = 'width:%dpx; height:%dpx;' % ( xmonParams.inputs['width'], xmonParams.inputs['height'] )
    tooltipstyle = 'font-size:90%; margin-left:5px; margin-top:10px; line-height:120%; left:10px; top:10px; color:black; '
#	    tooltipstyle = 'font-size:90%; position:absolute; left:10px; top:10px; color:black; '

    # Open table
    tab = xhu.Print(tab, '<table style="empty-cells: show; table-layout:fixed;">')
    tab = xhu.Print(tab, '<tr>')

    # New column -- Put tooltip box
    tab = xhu.Print(tab, '<td width=250 style="background:#DDE; text-align:center; vertical-align:top;">')
    tab = xhu.Print(tab, '<font style="color:#448; line-height:100%; font-weight:normal;">')
    tab = xhu.Print(tab, 'Detail box for the selected LB')
    tab = xhu.Print(tab, '<span style="font-size:90%;" class="sc">')
    tab = xhu.Print(tab, '<br/> try <b>hovering</b> over a data point!')
    tab = xhu.Print(tab, '<br/> try <b>zooming</b> inside the plot!')
    tab = xhu.Print(tab, '<br/> try <b>clicking</b> the trigger name!')
    tab = xhu.Print(tab, '</span>')
    tab = xhu.Print(tab, '</font>')
    tab = xhu.Print(tab, '<div style="position:relative;">')
    tab = xhu.Print(tab, '<div id="xmonTooltip%d" align="left" style="%s"></div>' % ( chartNumber, tooltipstyle ))
    tab = xhu.Print(tab, '</div>')
    tab = xhu.Print(tab, '</td>')

    # New column -- Put plot -- table on for the right half
    tab = xhu.Print(tab, '<td>')
#	    tab = xhu.Print(tab, '<table>')
#	    tab = xhu.Print(tab, '<tr>')
#	    tab = xhu.Print(tab, '<td>')
    tab = xhu.Print(tab, '<div id="xmonChart%d" style="%s"></div>' % ( chartNumber, plotstyle ))
#	    tab = xhu.Print(tab, '</td>')
#	    tab = xhu.Print(tab, '</tr>')
#	    tab = xhu.Print(tab, '</table>')
    tab = xhu.Print(tab, '</td>')

    # Close table
    tab = xhu.Print(tab, '</tr>')
    tab = xhu.Print(tab, '</table>')
    return tab


#==========================================================================
# Used by body()
# Uses printTriggers(), printRunranges()
#
def printCustomize(tab = '', xmonParams=None):

    rowstyle = ''

    blocktext = dict()
    blocktext['trig']   = 'L1, L2 & EF trigger list (double click to select/unselect)'
    blocktext['run']    = 'Run range (comma or dash)'
    blocktext['null']   = ''

    # Form
    tab = xhu.Print(tab, '<form name="customForm" method="get" action="%s/cgi-bin/xmon.cgi" onsubmit="selectAllOptions(%s);">' % (link['site'], trig_to_restId))

    # Table
    tab = xhu.Print(tab, '<table style="border-collapse:collapse; width:90%; text-align:center;">')
    tab = xhu.Print(tab, '<tr>')
    for block in ['trig', 'null', 'run']:
        if block=='null': tab = xhu.Print(tab, '<td width=75px>')
        else: tab = xhu.Print(tab, '<td width=400px style="vertical-align:top; text-align:center;">')
        tab = xhu.Print(tab, '<font style="color:#448;">')
        tab = xhu.Print(tab, '<br/>')
        tab = xhu.Print(tab, '%s' % blocktext[block])
        tab = xhu.Print(tab, '</font>')
        tab = xhu.Print(tab, '<br/>')
        if block=='trig': tab = printTriggers(tab, xmonParams)
        if block=='run':  tab = printRunranges(tab, xmonParams)
        tab = xhu.Print(tab, '</td>')

    tab = xhu.Print(tab, '</tr>')
#
#    # New row
#    tab = xhu.Print(tab, '<tr>')
#    tab = xhu.Print(tab, '<td><font style="color:#448">Bonus material</font></td>')
#    tab = xhu.Print(tab, '</tr>')
#
#    # Yourself
#    tab = xhu.Print(tab, '<tr>')
#    tab = xhu.Print(tab, '<td colspan=4>')
#    tab = xhu.Print(tab, '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For do-it-yourself enthusiasts, this form puts together web commands, e.g.,<br/>')
#    tab = xhu.Print(tab, '<ul>')
#    tab = xhu.Print(tab, '<li>%s<a style="color:blue;" href=%s>%s</a></li>' %
#                    ('https://cern.ch/x/cgi-bin/xmon.cgi?',
#                     'https://cern.ch/x/cgi-bin/xmon.cgi?run=178109&trig=L1_EM3',
#                     '<b>run</b>=178109&<b>trig</b>=L1_EM3'))
#    tab = xhu.Print(tab, '<li>%s<a style="color:blue;" href=%s>%s</a></li>' %
#                    ('https://cern.ch/x/cgi-bin/xmon.cgi?',
#                     'https://cern.ch/x/cgi-bin/xmon.cgi?run=178109&trig=L1_EM3,L1_J10,EF_mu20&logy=0',
#                     '<b>run</b>=178109&<b>trig</b>=L1_EM3,L1_J10,EF_mu20&<b>logy</b>=0'))
#    tab = xhu.Print(tab, '</ul>')
#    tab = xhu.Print(tab, '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;with unspecified fields taking the default values.')
#    tab = xhu.Print(tab, '</td>')
#    tab = xhu.Print(tab, '</tr>')
#
#    tab = xhu.Print(tab, '<tr style="height:10px;">')
#    tab = xhu.Print(tab, '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Feel free to create your own combination to bookmark.')
#    tab = xhu.Print(tab, '</tr>')
#
#    # Yourself-2
#    tab = xhu.Print(tab, '<tr>')
#    tab = xhu.Print(tab, '<td colspan=4>')
#    tab = xhu.Print(tab, '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;You can also execute them on LXPLUS, e.g.,<br/>')
#    tab = xhu.Print(tab, '<ul>')
#    tab = xhu.Print(tab, '<li>[lxplus] export XMONDIR=%s</li>' % '/afs/cern.ch/user/x/xmon/www/cgi-bin')
#    tab = xhu.Print(tab, '<li>[lxplus] $XMONDIR/xmon.cgi "%s" &gt; myoptions1.html</li>' % ('<span style="color:blue;"><b>run</b>=178109&<b>trig</b>=L1_EM3</span>'))
#    tab = xhu.Print(tab, '<li>[lxplus] $XMONDIR/xmon.cgi "%s" &gt; myoptions2.html</li>' % ('<span style="color:blue;"><b>run</b>=178109&<b>trig</b>=L1_EM3,L1_J10,EF_mu20&<b>logy</b>=0</span>'))
#    tab = xhu.Print(tab, '</ul>')
#    tab = xhu.Print(tab, '</td>')
#    tab = xhu.Print(tab, '</tr>')
#

    # Close table
    tab = xhu.Print(tab, '</table>')

    # Close form
    tab = xhu.Print(tab, '</form>')

    tab = xhu.Print(tab,'<!-- End customize tab -->')

    return tab


#==========================================================================
# Used by printCustomize()
# Uses None
#
def printTriggers(tab = '', xmonParams=None, virtual = ''):

    if len(virtual) > 0:
        tab = xhu.Print(tab, '<!--#include virtual="%s" -->' % virtual)
        return tab

    # Get tree
    tchain = xmonParams.inputs['tchain']
    if not tchain:                   return xhu.Print(tab, '<!-- No TChain, so no trigger list -->')
    if not tchain.GetListOfLeaves(): return xhu.Print(tab, '<!-- No TChain.GetListOfLeaves(), so no triggers list -->')

    # Available variables
    varlist = []
    for leaf in tchain.GetListOfLeaves():
        leafName = leaf.GetName()
        if 'xbp' in leafName:
            varlist.append(leafName.split( 'xbp__' )[1])

    varlist.sort()

    # Open table
    tab = xhu.Print(tab, '<table>')

    # Row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td>')
    tab = xhu.Print(tab, '<p class="vert">Selected<br/><span class="sc">trig</span></p>')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '<td>')
    tab = xhu.Print(tab, '<select id="trigId" name="trig" width=400 valign=top style="width:400px;" multiple size=15 onDblClick="moveOptions(%s);">' % trig_to_restId)
    for leaf in varlist:
        if leaf in xmonParams.inputs['varlist']['trig']['name']:
            tab = xhu.Print(tab, '<option value=%s>%s</option>' % (leaf, leaf))

    tab = xhu.Print(tab, '</select>')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '</tr>')

    # L1 Row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td>')
    tab = xhu.Print(tab, '<p class="vert">All<br/><span class="sc">trig</span></p>')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '<td>')
    tab = xhu.Print(tab, '<select id="restId" name="rest" width=400 valign=top style="width:400px;" multiple size=15 onDblClick="moveOptions(%s);">' % rest_to_trigId)
    for leaf in varlist:
        if leaf not in xmonParams.inputs['varlist']['trig']['name']:
            #if leaf.startswith('L1_'):
	    tab = xhu.Print(tab, '<option value=%s>%s</option>' % (leaf, leaf))

    tab = xhu.Print(tab, '</select>')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '</tr>')



    # Button
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td>')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '<td>')
#	    tab = xhu.Print(tab, '<input type="button" name="select" value="Move up" onclick="moveOptions(%s);"/>' % rest_to_trigId)
#	    tab = xhu.Print(tab, '<input type="button" name="unselect" value="Move down" onclick="moveOptions(%s);"/>' % trig_to_restId)
#	    tab = xhu.Print(tab, '<br/>')
#	    tab = xhu.Print(tab, 'Filter:')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.reset()" title="Clear the filter">Clear</a>&nbsp;')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_A\')" title="Show triggers starting with A">A</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_B\')" title="Show triggers starting with B">B</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_C\')" title="Show triggers starting with C">C</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_D\')" title="Show triggers starting with D">D</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_E\')" title="Show triggers starting with E">E</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_F\')" title="Show triggers starting with F">F</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_G\')" title="Show triggers starting with G">G</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_H\')" title="Show triggers starting with H">H</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_I\')" title="Show triggers starting with I">I</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_J\')" title="Show triggers starting with J">J</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_K\')" title="Show triggers starting with K">K</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_L\')" title="Show triggers starting with L">L</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_M\')" title="Show triggers starting with M">M</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_N\')" title="Show triggers starting with N">N</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_O\')" title="Show triggers starting with O">O</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_P\')" title="Show triggers starting with P">P</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_Q\')" title="Show triggers starting with Q">Q</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_R\')" title="Show triggers starting with R">R</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_S\')" title="Show triggers starting with S">S</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_T\')" title="Show triggers starting with T">T</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_U\')" title="Show triggers starting with U">U</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_V\')" title="Show triggers starting with V">V</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_W\')" title="Show triggers starting with W">W</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_X\')" title="Show triggers starting with X">X</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_Y\')" title="Show triggers starting with Y">Y</a>')
#	    tab = xhu.Print(tab, '<a href="javascript:customFilter.set(\'^??_Z\')" title="Show triggers starting with Z">Z</a>')
#	    tab = xhu.Print(tab, '<br/>')
    tab = xhu.Print(tab, 'Match this pattern &rarr; <input name="regexp" onKeyUp="customFilter.set(this.value)"/>')
#	    tab = xhu.Print(tab, '<input type="button" onClick="customFilter.set(this.form.regexp.value)" value="Filter">')
    tab = xhu.Print(tab, '<input type="button" onClick="customFilter.reset();this.form.regexp.value=\'\'" value="Clear"/>')
    tab = xhu.Print(tab, '<br/>')
#	    tab = xhu.Print(tab, '<input type=checkbox name="toLowerCase" onClick="custumFilter.set_ignore_case(!this.checked)"/> Case-sensitive')
    tab = xhu.Print(tab, '<script TYPE="text/javascript">')
    tab = xhu.Print(tab, '// Note: if you have a very large select list,')
    tab = xhu.Print(tab, '// you should deactivate the real-time filtering')
    tab = xhu.Print(tab, '// on the INPUT field below - remove the onKeyUp attribute.')
    tab = xhu.Print(tab, '<!--')
    tab = xhu.Print(tab, 'var customFilter = new filterlist(document.customForm.rest);')
    tab = xhu.Print(tab, '//-->')
    tab = xhu.Print(tab, '</script>')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '</tr>')

    # Close table
    tab = xhu.Print(tab, '</table>')
    return tab


#==========================================================================
def printRadioOption(tab, inputs, name, value, description, disabled=False):

    selected = ''
    notavail = ''
    if disabled:
        selected = 'disabled'
        description = '<s>' + description + '</s>'
    else:
        if inputs[name] == value:
            selected = 'checked="checked"'

    return xhu.Print(tab, '<br/><input type="radio" name="%s" value="%s" %s/><span class="sc">%s</span>, %s %s'
                    % (name, value, selected, value, description, comingsoon if disabled else ''))


#==========================================================================
# Used by printCustomize()
# Uses None
#
def printRunranges(tab='', xmonParams=None, virtual = ''):

    if len(virtual) > 0:
        tab = xhu.Print(tab, '<!--#include virtual="%s" -->' % virtual)
        return tab

    # Shorthands
    checked  = 'checked="checked"'
    disabled = 'disabled'
    inputs   = xmonParams.inputs

    tab = xhu.Print(tab, '<table>')

    # Row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td>')
    tab = xhu.Print(tab, '<p class="vert">')
    tab = xhu.Print(tab, '<span class="sc">run</span>')
    tab = xhu.Print(tab, '</p>')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '<td>')
    tab = xhu.Print(tab, '<textarea rows="1" cols="40" name="%s">%s</textarea>' %
                    ('run', ','.join(xmonParams.inputs['run'])))
    tab = xhu.Print(tab, '<br/>')
    tab = xhu.Print(tab, '<input type="text" size="5" name="%s" value="%s"/>=<span class="sc">%s</span> %s' %
                    ('lbsample', xmonParams.inputs['lbsample'], 'lbsample', '(auto is nrun&times;2)'))
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '</tr>')

    # Row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td>')
    tab = xhu.Print(tab, '<p class="vert">')
    tab = xhu.Print(tab, '<span class="sc">mode</span>')
    tab = xhu.Print(tab, '</p>')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '<td>')
    tab = printRadioOption(tab, inputs, 'mode', 'merge', 'Compare trig. only')
    tab = printRadioOption(tab, inputs, 'mode', 'compare', 'Compare runs &amp; trig')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '</tr>')

    # Row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td>')
    tab = xhu.Print(tab, '<p class="vert">')
    tab = xhu.Print(tab, '<span class="sc">ps</span>')
    tab = xhu.Print(tab, '</p>')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '<td>')
    tab = printRadioOption(tab, inputs, 'ps', 'bp', 'Rate &amp; x-sec. input values')
    tab = printRadioOption(tab, inputs, 'ps', 'ap', 'Rate &amp; x-sec. after-ps values')
    tab = printRadioOption(tab, inputs, 'ps', 'av', 'Rate &amp; x-sec. output values')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '</tr>')

    # New row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td>')
    tab = xhu.Print(tab, '<p class="vert">')
    tab = xhu.Print(tab, '<span class="sc">logy</span>')
    tab = xhu.Print(tab, '</p>')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '<td>')
    tab = printRadioOption(tab, inputs, 'logy', '1', 'Log y-axis')
    tab = printRadioOption(tab, inputs, 'logy', '0', 'Linear y-axis')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '</tr>')

    # New row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td>')
    tab = xhu.Print(tab, '<p class="vert">')
    tab = xhu.Print(tab, '<span class="sc">page</span>')
    tab = xhu.Print(tab, '</p>')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '<td>')
    tab = printRadioOption(tab, inputs, 'page', 'full', 'Show default layout')
    tab = printRadioOption(tab, inputs, 'page', 'chart', 'Show all on one page')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '</tr>')

    # New row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td>')
    tab = xhu.Print(tab, '<p class="vert">')
    tab = xhu.Print(tab, '<span class="sc">ntup</span>')
    tab = xhu.Print(tab, '</p>')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '<td>')
    tab = printRadioOption(tab, inputs, 'ntup', 'cool', 'Use COOL-derived xmon ntuples')
    tab = printRadioOption(tab, inputs, 'ntup', 'trp',  'Use TRP-derived xmon ntuples')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '</tr>')


   # Submit button
    tab = xhu.Print(tab, '<tr style="height:50px; vertical-align:bottom;">')
    tab = xhu.Print(tab, '<td colspan=2 style="text-align:center;">')
    tab = xhu.Print(tab, '<input type="submit" value="Submit" style="color:black; background:#AAE;" />')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '</tr>')

    # Close table
    tab = xhu.Print(tab, '</table>')
    return tab



#==========================================================================
def printAbout(tab='', site=link['site'], virtual=''):

    if len(virtual)>0:
        return xhu.Print(tab, '<!--#include virtual="%s" -->' % virtual)

    begintab = tab
    tab = xhu.Print(tab, '<!-- BEGIN About with (tab=%d) -->' % len(begintab) )
    tab = xhu.Print(tab,'<p>')
    tab = xhu.Print(tab,'<a href="%s">' % link['outreach'])
    tab = xhu.Print(tab,'<img src="%s/images/tmhong.jpg" alt="Photo of %s"/>' % (site, author))
    tab = xhu.Print(tab,'</a>')
    tab = xhu.Print(tab,'</p>')

    tab = xhu.Print(tab,'<p style="font-weight:normal;">')
    tab = xhu.Print(tab,'Created and maintained by')
    tab = xhu.Print(tab,'<a href="%s">%s</a> (pictured)' % (link['author'], author))
    tab = xhu.Print(tab,' and ')
    tab = xhu.Print(tab,'<a href="%s">%s</a> (not pictured & not the other person)' % (link['author2'], author2))
    tab = xhu.Print(tab,' at')
    tab = xhu.Print(tab,'<br/>')
    tab = xhu.Print(tab,'<br/>')
    tab = xhu.Print(tab,'<a href="http://www.hep.upenn.edu/">')
    tab = xhu.Print(tab,'<img src="%s/images/penn.gif" alt="UPenn logo" border=0/>' % site)
    tab = xhu.Print(tab,'</a>')
    tab = xhu.Print(tab,'</p>')
    tab = xhu.Print(tab, '<!-- END About (tab=%d begintab=%d same=%s) -->' % (len(tab), len(begintab), 'YES' if len(tab)==len(begintab) else 'NO') )

    return tab


#==========================================================================
# Used by printAllcharts()
# Uses None
#
def printTutorial(tab = '', site=link['site'], virtual=''):

    if len(virtual)>0:
        return xhu.Print(tab, '<!--#include virtual="%s" -->' % virtual)

    # Open table
    tab = xhu.Print(tab, '<table style="width:100%;">')

    # New row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td class="tutorial">&nbsp;How <b>xmon</b> works</td>')
    tab = xhu.Print(tab, '</tr>')
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td>')  # <-- Start mini-table
    tab = xhu.Print(tab, '<table class="smaller" style="text-align:center;">')

    # New mini-row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<th>Web interface</th>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<th>ROOT interface</th>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<th>DB interface</th>')
    tab = xhu.Print(tab, '</tr>')

    # New mini-row
    tab = xhu.Print(tab, '<tr style="height:10px;"">')
    tab = xhu.Print(tab, '</tr>')

    # New mini-row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td class="flowchart"> On-demand <br/>(web or cmd-line)</td>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td class="flowchart"> Updates ~%d min' % updatefreq)
    tab = xhu.Print(tab, '<br/>(<a href="%s">acrontab</a>)' % link['acrontablist'])
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td class="flowchart">ATLAS Detector</td>')
    tab = xhu.Print(tab, '<td style="width:20px;"></td>')
    tab = xhu.Print(tab, '<th>Inputs</th>')
    tab = xhu.Print(tab, '</tr>')

    # New mini-row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td style="text-align:center;"> &darr; </td>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td style="text-align:center;"> &darr; </td>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td style="text-align:center;"> &darr; </td>')
    tab = xhu.Print(tab, '</tr>')

    # New mini-row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td class="flowchart">')
    tab = xhu.Print(tab, 'Env. var.')
    tab = xhu.Print(tab, '<br/>(show <a href="%s/cgi-bin/setup.cgi">setup</a>)' % site)
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '<td style="text-align:center;"> &rArr; </td>')
    tab = xhu.Print(tab, '<td class="flowchart">xmon scripts</td>')
    tab = xhu.Print(tab, '<td> &larr; </td>')
    tab = xhu.Print(tab, '<td class="flowchart">xmon ROOT files')
    tab = xhu.Print(tab, '<br/>(<a href="%s">makeRoot.py</a>)' % link['makeRoot.py'])
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '<td> &larr; </td>')
    tab = xhu.Print(tab, '<td class="flowchart">')
    tab = xhu.Print(tab, '<a href="%s">COOL</a> or ' % link['COOL'])
    tab = xhu.Print(tab, '<a href="%s">TRP</a> DB' % link['TRP'])
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '<td>')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '<th>Server-side processing</th>')
    tab = xhu.Print(tab, '</tr>')

    # New mini-row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td style="text-align:center;"> &darr; </td>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td style="text-align:center;"> &darr; </td>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td style="text-align:center;"> &darr; </td>')
    tab = xhu.Print(tab, '</tr>')

    # New mini-row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td class="flowchart">')
    tab = xhu.Print(tab, 'Plug-ins')
    tab = xhu.Print(tab, '<br/> (<a href="http://www.highcharts.com">Highcharts&nbsp;JS</a>)')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '<td> &rArr; </td>')
    tab = xhu.Print(tab, '<td style="background:#DDE;" class="flowchart">HTML output')
    tab = xhu.Print(tab, '<br/> (<a href="%s">xmon.cgi</a>)' % link['xmon.cgi'])
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td style="background:#DDE;" class="flowchart">TCanvas output')
    tab = xhu.Print(tab, '<br/>(<a href="">TBD</a>)')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td style="background:#DDE;" class="flowchart">Text output')
    tab = xhu.Print(tab, '<br/>(<a href="%s">exampleCost.py</a>)' % link['exampleCost.py'])
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<th>Client-side processing</th>')
    tab = xhu.Print(tab, '</tr>')

    # New mini-row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td style="text-align:center;"> &darr; </td>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td style="text-align:center;"> &darr; </td>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td style="text-align:center;"> &darr; </td>')
    tab = xhu.Print(tab, '</tr>')

    # New mini-row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td style="background:black; color:white;" class="flowchart">')
    tab = xhu.Print(tab, 'This website<br/>(<a href="http://cern.ch/x" style="color:yellow;">http://cern.ch/x</a>)')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td style="background:black; color:white;" class="flowchart">')
    tab = xhu.Print(tab, 'User terminal')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<td style="background:black; color:white;" class="flowchart">')
    tab = xhu.Print(tab, 'User terminal')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '<td></td>')
    tab = xhu.Print(tab, '<th> User </th>')
    tab = xhu.Print(tab, '</tr>')

    # Close table
    tab = xhu.Print(tab, '</table>')
    tab = xhu.Print(tab, '<br/>')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '</tr>')

    # New row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td class="tutorial">&nbsp;How to use the website</td>')
    tab = xhu.Print(tab, '</tr>')
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<th><img width="700" src="%s/images/tutorial.png"/></th>' % site)
    tab = xhu.Print(tab, '</tr>')

    # New row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td class="tutorial">&nbsp;Structure of the <b>xmon</b> ROOT files</td>')
    tab = xhu.Print(tab, '</tr>')
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td>')
    tab = xhu.Print(tab, '<br/>')
    tab = xhu.Print(tab, '178109.root is named for the run number.')
    tab = xhu.Print(tab, '<br/>')
    tab = xhu.Print(tab, '<br/>')
    tab = xhu.Print(tab, '<table style="font-size:80%;">')
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<th colspan=4 style="border:1px solid;">LB information</th>')
    tab = xhu.Print(tab, '<th colspan=3 style="border:1px solid;">Trigger counts</th>')
    tab = xhu.Print(tab, '<th colspan=2 style="border:1px solid;">Rates (Hz)</th>')
    tab = xhu.Print(tab, '<th colspan=1 style="border:1px solid;">Cross-sections (mb)</th>')
    tab = xhu.Print(tab, '</tr>')
    tab = xhu.Print(tab, '<tr style="height:40px;"></tr>')
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td class="diag">evt__time</td>')
    tab = xhu.Print(tab, '<td class="diag">evt__lb</td>')
    tab = xhu.Print(tab, '<td class="diag">evt__bunchlumi</td>')
    tab = xhu.Print(tab, '<td class="diag">evt__lumi</td>')
    tab = xhu.Print(tab, '<td class="diag">tbp__L1_EM3</td>')
    tab = xhu.Print(tab, '<td class="diag">tap__L1_EM3</td>')
    tab = xhu.Print(tab, '<td class="diag">tav__L1_EM3</td>')
    tab = xhu.Print(tab, '<td class="diag">rbp__L1_EM3</td>')
    tab = xhu.Print(tab, '<td class="diag">rap__L1_EM3</td>')
    tab = xhu.Print(tab, '<td class="diag">xbp__L1_EM3</td>')
    tab = xhu.Print(tab, '</tr>')
    tab = xhu.Print(tab, '<tr style="height:40px;"></tr>')
    tab = xhu.Print(tab, '<tr><td>12864977</td><td>71</td><td>1.97e+29</td><td>4.58e+31</td><td>3030588</td><td>1212</td><td>1211</td><td>25053</td><td>10</td><td>4.522</td></tr>')
    tab = xhu.Print(tab, '<tr><td>12864979</td><td>72</td><td>3.76e+29</td><td>8.76e+31</td><td>5650060</td><td>2260</td><td>2256</td><td>46661</td><td>18</td><td>4.398</td></tr>')
    tab = xhu.Print(tab, '<tr><td>12864981</td><td>74</td><td>3.81e+29</td><td>8.88e+31</td><td>5692471</td><td>2277</td><td>2270</td><td>47229</td><td>18</td><td>4.415</td></tr>')
    tab = xhu.Print(tab, '<tr><td>12864983</td><td>76</td><td>3.8e+29</td><td>8.85e+31</td><td>5659144</td><td>2264</td><td>2258</td><td>47032</td><td>18</td><td>4.417</td></tr>')
    tab = xhu.Print(tab, '<tr><td>12864984</td><td>78</td><td>3.79e+29</td><td>8.82e+31</td><td>5608927</td><td>2244</td><td>2238</td><td>46706</td><td>18</td><td>4.408</td></tr>')
    tab = xhu.Print(tab, '<tr><td>12864986</td><td>81</td><td>3.77e+29</td><td>8.78e+31</td><td>5616231</td><td>16047</td><td>15796</td><td>46454</td><td>132</td><td>4.375</td></tr>')
    tab = xhu.Print(tab, '<tr><td>12864988</td><td>83</td><td>3.76e+29</td><td>8.76e+31</td><td>5596518</td><td>12437</td><td>12317</td><td>46304</td><td>102</td><td>4.374</td></tr>')
    tab = xhu.Print(tab, '<tr><td>12864989</td><td>84</td><td>3.75e+29</td><td>8.74e+31</td><td>5593915</td><td>12431</td><td>12397</td><td>46202</td><td>102</td><td>4.366</td></tr>')
    tab = xhu.Print(tab, '<tr><td>12864990</td><td>85</td><td>3.74e+29</td><td>8.72e+31</td><td>5561971</td><td>12361</td><td>12290</td><td>45974</td><td>102</td><td>4.358</td></tr>')
    tab = xhu.Print(tab, '<tr><td>12864992</td><td>86</td><td>3.73e+29</td><td>8.7e+31</td><td>5548943</td><td>12331</td><td>12228</td><td>45852</td><td>101</td><td>4.354</td></tr>')
    tab = xhu.Print(tab, '<tr><td>12864993</td><td>87</td><td>3.73e+29</td><td>8.68e+31</td><td>5535488</td><td>12301</td><td>12259</td><td>45746</td><td>101</td><td>4.355</td></tr>')
    tab = xhu.Print(tab, '<tr><td>12864994</td><td>88</td><td>3.72e+29</td><td>8.66e+31</td><td>5535204</td><td>12301</td><td>11272</td><td>45761</td><td>101</td><td>4.367</td></tr>')
    tab = xhu.Print(tab, '<tr><td>12864995</td><td>89</td><td>3.71e+29</td><td>8.64e+31</td><td>5534040</td><td>12297</td><td>12027</td><td>45745</td><td>101</td><td>4.376</td></tr>')
    tab = xhu.Print(tab, '<tr><td>12864997</td><td>90</td><td>3.7e+29</td><td>8.63e+31</td><td>5515046</td><td>12255</td><td>9848</td><td>45580</td><td>101</td><td>4.368</td></tr>')
    tab = xhu.Print(tab, '<tr><td>12864998</td><td>91</td><td>3.69e+29</td><td>8.61e+31</td><td>5499945</td><td>12221</td><td>12166</td><td>45431</td><td>100</td><td>4.36</td></tr>')
    tab = xhu.Print(tab, '<tr><td>12864999</td><td>92</td><td>3.69e+29</td><td>8.59e+31</td><td>5475012</td><td>12167</td><td>12131</td><td>45262</td><td>100</td><td>4.355</td></tr>')
    tab = xhu.Print(tab, '<tr><td>12865000</td><td>93</td><td>3.68e+29</td><td>8.58e+31</td><td>5468389</td><td>12152</td><td>12107</td><td>45205</td><td>100</td><td>4.356</td></tr>')
    tab = xhu.Print(tab, '<tr><td>12865002</td><td>94</td><td>3.67e+29</td><td>8.56e+31</td><td>5470249</td><td>12156</td><td>11526</td><td>45219</td><td>100</td><td>4.367</td></tr>')
    tab = xhu.Print(tab, '<tr><td>12865002</td><td>95</td><td>3.67e+29</td><td>8.54e+31</td><td>5463196</td><td>12140</td><td>12021</td><td>45128</td><td>100</td><td>4.364</td></tr>')
    tab = xhu.Print(tab, '<tr><td>12865003</td><td>96</td><td>3.66e+29</td><td>8.53e+31</td><td>5455035</td><td>12121</td><td>12087</td><td>45090</td><td>100</td><td>4.371</td></tr>')
    tab = xhu.Print(tab, '<tr><td>12865006</td><td>98</td><td>3.65e+29</td><td>8.5e+31</td><td>5393107</td><td>13483</td><td>13426</td><td>44909</td><td>112</td><td>4.399</td></tr>')
    tab = xhu.Print(tab, '<tr><td>12865007</td><td>99</td><td>3.64e+29</td><td>8.48e+31</td><td>5424243</td><td>13559</td><td>13517</td><td>44819</td><td>112</td><td>4.365</td></tr>')
    tab = xhu.Print(tab, '<tr><td>12865008</td><td>100</td><td>3.63e+29</td><td>8.47e+31</td><td>5420593</td><td>13551</td><td>13233</td><td>44774</td><td>111</td><td>4.369</td></tr>')
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td>')
    tab = xhu.Print(tab, '<td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td>')
    tab = xhu.Print(tab, '</tr>')
    tab = xhu.Print(tab, '</table>')
    tab = xhu.Print(tab, '<br/>')
    tab = xhu.Print(tab, '<br/>')
    tab = xhu.Print(tab, 'Explanation:')
    tab = xhu.Print(tab, '<pre class="smallest">')
    tab = xhu.Print(tab, 'evt = information for this lumi-block period')
    tab = xhu.Print(tab, 'tbp = trigger counts before prescaling')
    tab = xhu.Print(tab, 'tap = trigger counts after prescaling')
    tab = xhu.Print(tab, 'tav = trigger counts after veto-ing')
    tab = xhu.Print(tab, 'rbp = trigger rates before prescaling')
    tab = xhu.Print(tab, 'rap = trigger rates counts after prescaling')
    tab = xhu.Print(tab, 'rav = trigger rates after veto-ing')
    tab = xhu.Print(tab, 'xbp = trigger cross-section before prescaling')
    tab = xhu.Print(tab, 'xap = trigger cross-section counts after prescaling')
    tab = xhu.Print(tab, 'xav = trigger cross-section after veto-ing')
    tab = xhu.Print(tab, '</pre>')
    tab = xhu.Print(tab, '<br/>')
    tab = xhu.Print(tab, 'ROOT session:')
    tab = xhu.Print(tab, '<pre class="smallest">')
    tab = xhu.Print(tab, 'ntp1.Scan(var, cut, fmt)')
    tab = xhu.Print(tab, 'cut = "evt__lblength&gt;110&amp;&amp;evt__bunches&gt;10&amp;&amp;tav__L1_EM3&gt;1"')
    tab = xhu.Print(tab, 'fmt = "colsize=8 precision=4 col=d:d:d:d:10.3g:10.3g:10.3g:d:d:d:d:d:d:d";')
    tab = xhu.Print(tab, 'var = "evt__time:evt__lb:evt__bunchlumi:evt__lumi:" + \ ')
    tab = xhu.Print(tab, '      "tbp__L1_EM3:tap__L1_EM3:tav__L1_EM3:" + \ ')
    tab = xhu.Print(tab, '      "rbp__L1_EM3:rap__L1_EM3:rav__L1_EM3:" + \ ')
    tab = xhu.Print(tab, '      "xbp__L1_EM3:xap__L1_EM3:xav__L1_EM3"')
    tab = xhu.Print(tab, '</pre>')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '</tr>')

#	    # New row
#	    tab = xhu.Print(tab, '<tr>')
#	    tab = xhu.Print(tab, '<td class="tutorial">&nbsp;Structure of the <b>xmon</b> HTML files</td>')
#	    tab = xhu.Print(tab, '</tr>')
#	    tab = xhu.Print(tab, '<tr>')
#	    tab = xhu.Print(tab, '<td>')
#	    tab = xhu.Print(tab, '<br/>')
#	    tab = xhu.Print(tab, '<a href=%s>178109.html</a> is named for the run number.' % link['178109.html'])
#	    tab = xhu.Print(tab, '<br/>')
#	    tab = xhu.Print(tab, '<br/>')
#	    tab = xhu.Print(tab, '<pre class="smallest">')
#	    tab = xhu.Print(tab, '&lt;html&gt;')
#	    tab = xhu.Print(tab, '    &lt;head&gt;')
#	    tab = xhu.Print(tab, '        &lt;!--#include virtual="<a href=%s>https://cern.ch/x/html/includes.html</a>" --&gt;' % link['includes.html'])
#	    tab = xhu.Print(tab, '    &lt;/head&gt;')
#	    tab = xhu.Print(tab, '    &lt;body&gt;')
#	    tab = xhu.Print(tab, '        &lt;!--#include virtual="<a href=%s>https://cern.ch/x/html/header.html</a>" --&gt;' % link['header.html'])
#	    tab = xhu.Print(tab, '        &lt;!--#include virtual="<a href=%s>https://cern.ch/x/html/body.html</a>" --&gt;' % link['body.html'])
#	    tab = xhu.Print(tab, '        &lt;!--#include virtual="<a href=%s>https://cern.ch/x/html/footer.html</a>" --&gt;' % link['footer.html'])
#	    tab = xhu.Print(tab, '    &lt;/body&gt;')
#	    tab = xhu.Print(tab, '    &lt;script src="<a href=%s>https://cern.ch/x/js/178109.js</a>" type="text/javascript"&gt;&lt;/script&gt;' % link['178109.js'])
#	    tab = xhu.Print(tab, '&lt;/html&gt;')
    tab = xhu.Print(tab, '</pre>')
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '</tr>')

    # Close table
    tab = xhu.Print(tab, '</table>')

    return tab


#==========================================================================
def printFooter(tab='', site=link['site'], virtual='', xmonParams=None):

    if len(virtual)>0:
        return xhu.Print(tab, '<!--#include virtual="%s" -->' % virtual)

    #
    # Get information
    #

    timenow = datetime.datetime.utcnow().strftime('%a, %d %b %Y, %H:%M:%S UTC')
    lasttime = xlu.readLastTime()
    if len(lasttime) != 1:
        tab = xhu.Print(tab, '<!-- ERROR -- problem reading lasttime.txt : %s) -->' % lasttime)
        lasttime = ['']

    #
    # xhu.Print table
    #

    begintab = tab
    tab = xhu.Print(tab, '<!-- BEGIN Footer (tab=%d) -->' % len(begintab) )

#	    # Wait message
#	    tab = xhu.Print(tab, '<p style="text-align:center;">')
#	    tab = xhu.PrintNormal(tab, '<font color="red">&hearts;</font>&nbsp;%s' %
#	                          'If you see nothing, the page is loading...  Thank you for being patient.')
#	    tab = xhu.Print(tab, '</p>')

    # Begin table
    tab = xhu.Print(tab, '<table class="bottomtable" style="margin-right:4px; padding-right:4px;">')

    # Data
    login = xmonParams.inputs['login']
    email       = xmonParams.inputs['email']
    logout      = '<a class="whitelink" href="%s" title="Logout of CERN Single Sign-On">logout</a>' % link['logout']
    browser     = xmonParams.inputs['browser']
    ipaddress   = xmonParams.inputs['ipaddress']

    # Row
    tab = xhu.Print(tab, '<tr>')
    tab = xhu.Print(tab, '<td colspan=2 style="text-align:left">')
    tab = xhu.Print(tab, '<font face="%s">WELCOME:</font>' % fontface)
    tab = xhu.Print(tab, '<a href="#" title="%s, this is you!  You are logged in from %s using %s." class="selected">%s</a>'
                    % (email, ipaddress, browser, login))
    tab = xhu.Print(tab, '%s ' % logout)
    tab = xhu.Print(tab, '<font style="color:yellow;">&bull;</font> ')
    tab = xhu.Print(tab, 'Your favorite triggers: ')
    for trig in xmonParams.inputs['favtrigs']:
        tab = xhu.Print(tab, '%s' % trig)
    tab = xhu.Print(tab, '</td>')
    tab = xhu.Print(tab, '</tr>')

    # New row
    tab = xhu.Print(tab, '<tr style="vertical-align:top;">')

    # Item
    tab = xhu.Print(tab, '<td style="text-align:left">')
    tab = xhu.Print(tab, '<font face="%s">QUICK LINKS:</font>' % fontface)
    tab = xhu.Print(tab, '<a class="menuanchorclass" rel="sites">Useful</a>')
    tab = xhu.Print(tab, '<font style="color:yellow;">&bull;</font> ')
    tab = xhu.Print(tab, '<a class="menuanchorclass" rel="wikis">T<font style="font-variant:small-caps;">w</font>ikis</a>')
    #tab = xhu.Print(tab, '<font style="color:yellow;">&bull;</font> ')
    #tab = xhu.Print(tab, '<a class="menuanchorclass" rel="download">Download</a>')
    #tab = xhu.Print(tab, '<font style="color:yellow;">&bull;</font> ')
    #tab = xhu.Print(tab, '<a class="menuanchorclass" rel="help" style="color:yellow;">Help / FAQ</a>')
    tab = xhu.Print(tab, '</td>')

    # Item
    tab = xhu.Print(tab, '<td style="text-align:right">')
    #tab = xhu.Print(tab, '<font style="color:yellow;">&bull;</font> ')
    lastlb = ''
    lastrun = ''
    try:
        lastlb = str(xlu.readLastLB()[0])
        lastrun = str(lastlb.split('/')[0])
    except:
        pass
    #tab = xhu.Print(tab, 'Auto-updates ~%d min' % updatefreq)
    #tab = xhu.Print(tab, '&amp; latest run/LB is <a href="%s/cgi-bin/xmon.cgi?run=%s">%s</a>' % (site, lastrun, lastlb))
    tab = xhu.Print(tab, '</td>')

    # New row
    tab = xhu.Print(tab, '</tr>')
    tab = xhu.Print(tab, '<tr>')
#
#    # Item
    tab = xhu.Print(tab, '<td style="text-align:left">')
#    tab = xhu.Print(tab, '<font face="%s">CONTACT &amp; SUPPORT:</font>' % fontface)
#    tab = xhu.Print(tab, '<a class="whitelink" title="%s, this is me!" href="%s">%s</a>' % (link['author'], link['author'], author) )
#    tab = xhu.Print(tab, '</td>')
#
    # Item
##    tab = xhu.Print(tab, '<td style="text-align:right">')
##    tab = xhu.Print(tab, '<font style="color:yellow;">&bull;</font>')
##    tab = xhu.Print(tab, 'Using')
##    tab = xhu.Print(tab, '<a class="menuanchorclass" rel="codelist">code</a> ')
#	    tab = xhu.Print(tab, '<a class="whitelink" href="%s">TrigCostPython</a>' % link['TrigCostPython'])
#	    tab = xhu.Print(tab, '<a class="whitelink" href="%s">TrigXMonitor</a>' % link['TrigXMonitor'])
##    tab = xhu.Print(tab, '&rarr; <a href="%s">DB</a> on %s' % (link['DB'], lasttime[0])) # 'Mon, 21 Mar 2011, 10:14 UTC')
##    tab = xhu.Print(tab, '</td>')

    # Close row
    tab = xhu.Print(tab, '</tr>')

    # End table
    tab = xhu.Print(tab, '</table>')
    tab = xhu.Print(tab, '<!-- END Footer (tab=%d begintab=%d same=%s) -->' % (len(tab), len(begintab), 'YES' if len(tab)==len(begintab) else 'NO') )
    return tab


#==========================================================================
def test(tab= ''):
    tab = ''
    tab = printIncludes(tab)
#	    tab = printHeader(tab, link['site'], '')
    tab = printAbout(tab)
    tab = printTutorial(tab)
#	    tab = printFooter(tab)

#eof
