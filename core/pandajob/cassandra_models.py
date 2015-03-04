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
    actualcorecount = columns.Integer()
    assignedpriority = columns.Integer()
    atlasrelease = columns.Text()
    attemptnr = columns.Integer()
    batchid = columns.Text()
    brokerageerrorcode = columns.Integer()
    brokerageerrordiag = columns.Text()
    cloud = columns.Text()
    cmtconfig = columns.Text()
    commandtopilot = columns.Text()
    computingsite = columns.Text()
    computingelement = columns.Text()
    corecount = columns.Integer()
    countrygroup = columns.Text()
    cpuconsumptiontime = columns.BigInt()
    cpuconsumptionunit = columns.Text()
    cpuconversion = columns.Decimal()
    creationtime = columns.DateTime()
    creationhost = columns.Text()
    currentpriority = columns.Integer()
    date = columns.DateTime(index=True)
    ddmerrorcode = columns.Integer()
    ddmerrordiag = columns.Text()
    destinationdblock = columns.Text()
    destinationse = columns.Text()
    destinationsite = columns.Text()
    dispatchdblock = columns.Text()
    endtime = columns.DateTime()
    exeerrorcode = columns.Integer()
    exeerrordiag = columns.Text()
    grid = columns.Text()
    homepackage = columns.Text()
    inputfiletype = columns.Text()
    inputfileproject = columns.Text()
    inputfilebytes = columns.BigInt()
    ipconnectivity = columns.Text()
    jeditaskid = columns.BigInt()
    jobdispatchererrorcode = columns.Integer()
    jobdispatchererrordiag = columns.Text()                                  
    jobdefinitionid = columns.BigInt()
    jobexecutionid = columns.BigInt()
    jobmetrics = columns.Text()
    jobstatus = columns.Text()
    jobname = columns.Text()
    jobparameters = columns.Text()
    jobsetid = columns.BigInt()
    jobsubstatus = columns.Text()
    lockedby = columns.Text()
    maxattempt = columns.Integer()
    maxcpucount = columns.Integer()
    maxcpuunit = columns.Text()
    maxdiskcount = columns.Integer()
    maxdiskunit = columns.Text()
    minramcount = columns.Integer()
    minramunit = columns.Text()
    metadata = columns.Text()
    modificationtime = columns.DateTime()
    modificationhost = columns.Set(columns.Text) 
    nevents = columns.Integer()
    ninputdatafiles = columns.Integer()
    ninputfiles = columns.Integer()
    noutputdatafiles = columns.Integer()
    outputfilebytes = columns.BigInt()
    parentid = columns.BigInt()
    piloterrorcode = columns.Integer()
    piloterrordiag = columns.Text()
    pilotid = columns.Text()
    pilottiming = columns.Text()
    processingtype = columns.Text()
    proddblock = columns.Text()
    proddbupdatetime = columns.DateTime()
    prodserieslabel = columns.Text()
    prodsourcelabel = columns.Text()
    produserid = columns.Text()
    produsername = columns.Text()
    relocationflag = columns.Integer()
    schedulerid = columns.Text()
    sourcesite = columns.Text()
    specialhandling = columns.Text()
    starttime = columns.DateTime()
    statechangetime = columns.DateTime()
    superrorcode = columns.Integer()
    superrordiag = columns.Text()
    taskbuffererrorcode = columns.Integer()
    taskbuffererrordiag = columns.Text()
    taskid = columns.Integer()
    transexitcode = columns.Text()
    transfertype = columns.Text()
    transformation = columns.Text()
    vo = columns.Text()                                        
    workinggroup = columns.Text()
    workqueue_id = columns.Integer()


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
    diag = columns.Text(primary_key=True)
    count = columns.Counter()

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
    