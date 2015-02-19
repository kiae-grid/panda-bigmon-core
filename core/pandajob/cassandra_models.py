# Panda Jobs data model for Cassandra

from cqlengine import columns
from cqlengine.models import Model
from cqlengine import  SizeTieredCompactionStrategy

class jobs(Model):
    __compaction__ = SizeTieredCompactionStrategy
    __compaction_max_compaction_threshold__ = 32
    __compaction_min_compaction_threshold__ = 4
    __read_repair_chance__ = 0.0
    __dclocal_read_repair_chance__ = 0.1
    __default_time_to_live__ = 0
    __gc_grace_seconds__ = 864000
    __memtable_flush_period_in_ms__ = 0

    pandaid = columns.BigInt(primary_key=True)
    modificationtime = columns.DateTime()
    jobdefinitionid = columns.BigInt()
    schedulerid = columns.Text()
    pilotid = columns.Text()
    creationtime = columns.DateTime()
    creationhost = columns.Text()
    modificationhost = columns.Set(columns.Text) 
    atlasrelease = columns.Text()
    transformation = columns.Text()
    homepackage = columns.Text()
    prodserieslabel = columns.Text()
    prodsourcelabel = columns.Text()
    produserid = columns.Text()
    assignedpriority = columns.Integer()
    currentpriority = columns.Integer()
    attemptnr = columns.Integer()
    maxattempt = columns.Integer()
    jobstatus = columns.Text()
    jobname = columns.Text()
    maxcpucount = columns.Integer()
    maxcpuunit = columns.Text()
    maxdiskcount = columns.Integer()
    maxdiskunit = columns.Text()
    ipconnectivity = columns.Text()
    minramcount = columns.Integer()
    minramunit = columns.Text()
    starttime = columns.DateTime()
    endtime = columns.DateTime()
    cpuconsumptiontime = columns.BigInt()
    cpuconsumptionunit = columns.Text()
    commandtopilot = columns.Text()
    transexitcode = columns.Text()
    piloterrorcode = columns.Integer()
    piloterrordiag = columns.Text()
    exeerrorcode = columns.Integer()
    exeerrordiag = columns.Text()
    superrorcode = columns.Integer()
    superrordiag = columns.Text()
    ddmerrorcode = columns.Integer()
    ddmerrordiag = columns.Text()
    brokerageerrorcode = columns.Integer()
    brokerageerrordiag = columns.Text()
    jobdispatchererrorcode = columns.Integer()
    jobdispatchererrordiag = columns.Text()
    taskbuffererrorcode = columns.Integer()
    taskbuffererrordiag = columns.Text()
    computingsite = columns.Text()
    computingelement = columns.Text()
    jobparameters = columns.Blob()
    metadata = columns.Text()
    proddblock = columns.Text()
    dispatchdblock = columns.Text()
    destinationdblock = columns.Text()
    destinationse = columns.Text()
    nevents = columns.Integer()
    grid = columns.Text()
    cloud = columns.Text()
    cpuconversion = columns.Decimal()
    sourcesite = columns.Text()
    destinationsite = columns.Text()
    transfertype = columns.Text()
    taskid = columns.Integer()
    cmtconfig = columns.Text()
    statechangetime = columns.DateTime()
    proddbupdatetime = columns.DateTime()
    lockedby = columns.Text()
    relocationflag = columns.Integer()
    jobexecutionid = columns.BigInt()
    vo = columns.Text()
    pilottiming = columns.Text()
    workinggroup = columns.Text()
    processingtype = columns.Text()
    produsername = columns.Text()
    produsername_upper = columns.Text()
    ninputfiles = columns.Integer()
    countrygroup = columns.Text()
    batchid = columns.Text()
    parentid = columns.BigInt()
    specialhandling = columns.Text()
    jobsetid = columns.BigInt()
    corecount = columns.Integer()
    ninputdatafiles = columns.Integer()
    jobparameteres = columns.Blob()
    metadata = columns.Blob()
    ninputdatafiles = columns.Integer()
    inputfiletype = columns.Text()
    inputfileproject = columns.Text()
    inputfilebytes = columns.BigInt()
    noutputdatafiles = columns.Integer()
    outputfilebytes = columns.BigInt()
    jobmetrics = columns.Text()
    workqueue_id = columns.Integer()
    jeditaskid = columns.BigInt()

class day_site_errors_30m(Model):
    __compaction__ = SizeTieredCompactionStrategy
    __compaction_max_compaction_threshold__ = 32
    __compaction_min_compaction_threshold__ = 4
    __read_repair_chance__ = 0.0
    __dclocal_read_repair_chance__ = 0.1
    __default_time_to_live__ = 0
    __gc_grace_seconds__ = 864000
    __memtable_flush_period_in_ms__ = 0
    date = columns.DateTime(primary_key=True)
    computingsite = columns.Text(primary_key=True)
    base_mtime = columns.DateTime(primary_key=True)
    errcode = columns.Text(primary_key=True)
    count = columns.Counter()
    diag = columns.Text()

class day_index(Model):
    __compaction__ = SizeTieredCompactionStrategy
    __compaction_max_compaction_threshold__ = 32
    __compaction_min_compaction_threshold__ = 4
    __read_repair_chance__ = 0.0
    __dclocal_read_repair_chance__ = 0.1
    __default_time_to_live__ = 0
    __gc_grace_seconds__ = 864000
    __memtable_flush_period_in_ms__ = 0
    date = columns.DateTime(primary_key=True)
    modificationtime = columns.DateTime(primary_key=True)
    pandaid = columns.Integer(primary_key=True)
    