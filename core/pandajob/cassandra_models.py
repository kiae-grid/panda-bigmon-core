# Panda Jobs data model for Cassandra

from cqlengine import columns
from cqlengine.models import Model
from cqlengine import SizeTieredCompactionStrategy

"""
CQL statements for this table
=============================

CREATE TABLE bigpanda_archive.jobs (
    pandaid bigint PRIMARY KEY,
    actualcorecount int,
    assignedpriority int,
    atlasrelease text,
    attemptnr int,
    batchid text,
    brokerageerrorcode int,
    brokerageerrordiag text,
    cloud text,
    cmtconfig text,
    commandtopilot text,
    computingelement text,
    computingsite text,
    corecount int,
    countrygroup text,
    cpuconsumptiontime bigint,
    cpuconsumptionunit text,
    cpuconversion decimal,
    creationhost text,
    creationtime timestamp,
    currentpriority int,
    date timestamp,
    ddmerrorcode int,
    ddmerrordiag text,
    destinationdblock text,
    destinationse text,
    destinationsite text,
    dispatchdblock text,
    endtime timestamp,
    exeerrorcode int,
    exeerrordiag text,
    grid text,
    homepackage text,
    inputfilebytes bigint,
    inputfileproject text,
    inputfiletype text,
    ipconnectivity text,
    jeditaskid bigint,
    jobdefinitionid bigint,
    jobdispatchererrorcode int,
    jobdispatchererrordiag text,
    jobexecutionid bigint,
    jobmetrics text,
    jobname text,
    jobparameters text,
    jobsetid bigint,
    jobstatus text,
    jobsubstatus text,
    lockedby text,
    maxattempt int,
    maxcpucount int,
    maxcpuunit text,
    maxdiskcount int,
    maxdiskunit text,
    metadata text,
    minramcount int,
    minramunit text,
    modificationhost text,
    modificationtime timestamp,
    nevents int,
    ninputdatafiles int,
    ninputfiles int,
    noutputdatafiles int,
    outputfilebytes bigint,
    parentid bigint,
    piloterrorcode int,
    piloterrordiag text,
    pilotid text,
    pilottiming text,
    processingtype text,
    proddblock text,
    proddbupdatetime timestamp,
    prodserieslabel text,
    prodsourcelabel text,
    produserid text,
    produsername text,
    relocationflag int,
    schedulerid text,
    sourcesite text,
    specialhandling text,
    starttime timestamp,
    statechangetime timestamp,
    superrorcode int,
    superrordiag text,
    taskbuffererrorcode int,
    taskbuffererrordiag text,
    taskid int,
    transexitcode text,
    transfertype text,
    transformation text,
    vo text,
    workinggroup text,
    workqueue_id int
) WITH bloom_filter_fp_chance = 0.01
    AND caching = '{"keys":"ALL", "rows_per_partition":"NONE"}'
    AND comment = ''
    AND compaction = {'min_threshold': '4', 'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32'}
    AND compression = {'sstable_compression': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND dclocal_read_repair_chance = 0.1
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair_chance = 0.0
    AND speculative_retry = '99.0PERCENTILE';
CREATE INDEX jobs_date_idx ON bigpanda_archive.jobs (date);
"""

class jobs(Model):
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
    computingelement = columns.Text()
    computingsite = columns.Text()
    corecount = columns.Integer()
    countrygroup = columns.Text()
    cpuconsumptiontime = columns.BigInt()
    cpuconsumptionunit = columns.Text()
    cpuconversion = columns.Decimal()
    creationhost = columns.Text()
    creationtime = columns.DateTime()
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
    inputfilebytes = columns.BigInt()
    inputfileproject = columns.Text()
    inputfiletype = columns.Text()
    ipconnectivity = columns.Text()
    jeditaskid = columns.BigInt()
    jobdefinitionid = columns.BigInt()
    jobdispatchererrorcode = columns.Integer()
    jobdispatchererrordiag = columns.Text()
    jobexecutionid = columns.BigInt()
    jobmetrics = columns.Text()
    jobname = columns.Text()
    jobparameters = columns.Text()
    jobsetid = columns.BigInt()
    jobstatus = columns.Text()
    jobsubstatus = columns.Text()
    lockedby = columns.Text()
    maxattempt = columns.Integer()
    maxcpucount = columns.Integer()
    maxcpuunit = columns.Text()
    maxdiskcount = columns.Integer()
    maxdiskunit = columns.Text()
    metadata = columns.Text()
    minramcount = columns.Integer()
    minramunit = columns.Text()
    # XXX/rea: really columns.Set?
    modificationhost = columns.Set(columns.Text)
    modificationtime = columns.DateTime()
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

    __compaction__ = SizeTieredCompactionStrategy
    __compaction_max_compaction_threshold__ = 32
    __compaction_min_compaction_threshold__ = 4
    __dclocal_read_repair_chance__ = 0.1
    __default_time_to_live__ = 0
    __gc_grace_seconds__ = 864000
    __memtable_flush_period_in_ms__ = 0
    __read_repair_chance__ = 0.0


"""
CQL statements for this table
=============================

CREATE TABLE bigpanda_archive.day_errors_30m (
    date timestamp,
    base_mtime timestamp,
    "count" counter,
    PRIMARY KEY (date, base_mtime)
) WITH CLUSTERING ORDER BY (base_mtime ASC)
    AND bloom_filter_fp_chance = 0.01
    AND caching = '{"keys":"ALL", "rows_per_partition":"NONE"}'
    AND comment = ''
    AND compaction = {'min_threshold': '4', 'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32'}
    AND compression = {'sstable_compression': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND dclocal_read_repair_chance = 0.1
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair_chance = 0.0
    AND speculative_retry = '99.0PERCENTILE';
"""

class day_errors_30m(Model):

    date = columns.DateTime(primary_key = True)
    base_mtime = columns.DateTime(primary_key = True)
    count = columns.Counter()

    __compaction__ = SizeTieredCompactionStrategy
    __compaction_max_compaction_threshold__ = 32
    __compaction_min_compaction_threshold__ = 4
    __dclocal_read_repair_chance__ = 0.1
    __default_time_to_live__ = 0
    __gc_grace_seconds__ = 864000
    __memtable_flush_period_in_ms__ = 0
    __read_repair_chance__ = 0.0


"""
CQL statements for this table
=============================

CREATE TABLE panda_archive.day_site_errors_cnt (
    date timestamp,
    interval text,
    base_mtime timestamp,
    computingsite text,
    errcode text,
    diag text,
    err_count int,
    job_count int,
    PRIMARY KEY ((date, interval), base_mtime, computingsite, errcode, diag)
) WITH CLUSTERING ORDER BY (base_mtime ASC, computingsite ASC, errcode ASC, diag ASC)
    AND bloom_filter_fp_chance = 0.01
    AND caching = '{"keys":"ALL", "rows_per_partition":"NONE"}'
    AND comment = ''
    AND compaction = {'min_threshold': '4', 'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32'}
    AND compression = {'sstable_compression': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND dclocal_read_repair_chance = 0.1
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair_chance = 0.0
    AND speculative_retry = '99.0PERCENTILE';
"""

class day_site_errors_cnt(Model):
    date = columns.DateTime(primary_key = True)
    interval = columns.Text(primary_key = True)
    base_mtime = columns.DateTime(primary_key = True)
    computingsite = columns.Text(primary_key = True)
    errcode = columns.Integer(primary_key = True)
    diag = columns.Text(primary_key = True)
    err_count = columns.Counter()
    job_count = columns.Counter()

    __compaction__ = SizeTieredCompactionStrategy
    __compaction_max_compaction_threshold__ = 32
    __compaction_min_compaction_threshold__ = 4
    __dclocal_read_repair_chance__ = 0.1
    __default_time_to_live__ = 0
    __gc_grace_seconds__ = 864000
    __memtable_flush_period_in_ms__ = 0
    __read_repair_chance__ = 0.0
