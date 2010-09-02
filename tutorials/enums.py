
QUIZ_CHOICES = (
    (1, 'Quiz 1'),
    (2, 'Quiz 2'),
    (3, 'Quiz 3'),
    (4, 'Quiz 4'),
    (5, 'Quiz 5'),
    )

STAFF_CHOICES = (
    ('LA', 'Undergraduate Lab Assistant'),
    ('TA', 'Graduate Teaching Assistant'),
    ('Head TA', 'Head Teaching Assistant'),
    ('Lecturer', 'Lecturer'),
    ('Admin', 'Administrative Assistant'),
    )

SEMESTER_CHOICES = (
    ('', '--All Terms--'), 
    ('S10', 'Spring 2010'),
    ('F09', 'Fall 2009'),
    ('S09', 'Spring 2009'),
    ('F08', 'Fall 2008'),
    ('S08', 'Spring 2008'),
    ('F07', 'Fall 2007'),
    ('S07', 'Spring 2007'),
    ('F06', 'Fall 2006'),
    ('S06', 'Spring 2006'),
    ('F05', 'Fall 2005'),
    )

LAB_CHOICES = (
    (1, 'Lab 1'),
    (2, 'Lab 2'),
    (3, 'Lab 3'),
    (4, 'Lab 4'),
    (5, 'Lab 5'),
    (6, 'Lab 6'),
    (7, 'Lab 7'),
    (8, 'Lab 8'),
    (9, 'Design Project'),
    )

VIDEO_CHOICES = (
    ('', '-- All Video Types --'),
    ('Lecture', 'Lectures'),
    ('Section', 'Recitations'),
    ('OldQuiz', 'Past Quiz Problems'),
    ('LabHint', 'Lab Hints'),
    ('TutProb', 'Tutorial Problems'),
    ('Concept', 'Conceptual Reviews'),
    )

TOPIC_CHOICES = (
    ('', '-- All Topics --'),
    ('BasicsOfInformation', 'Basics of Information'),
    ('TheDigitalAbstraction', 'The Digital Abstraction'),
    ('CMOSTechnology', 'CMOS Technology'),
    ('GatesAndBooleanLogic', 'Gates And Boolean Logic'),
    ('SynthesisOfCombinationalLogic', 'Synthesis of Combinational Logic'),
    ('SequentialLogic', 'Sequential Logic'),
    ('FSMs', 'FSMs'),
    ('SynchronizationAndMetastability', 'Synchronization and Metastability'),
    ('Pipelining', 'Pipelining'),
    ('ModelsOfComputation','Models of Computation'),
    ('ProgrammableMachines', 'Programmable Machines'),
    ('MachineLanguage','Machine Language'),
    ('StacksAndProcedures','Stacks and Procedures'),
    ('BuildingTheBeta', 'Building the Beta'),
    ('MemoryHierarchy', 'Memory Hierarchy'),
    ('Caches','Caches'),
    ('VirtualMemory','Virtual Memory'),
    ('VirtualMachines','Virtual Machines and OS Issues'),
    ('DevicesInterruptsAndRealTime', 'Devices Interrupts and Real Time'),
    ('Semaphores','Semaphores'),
    ('PipelinedBeta','Pipelined Beta'),
    )



TUTORIAL_PROBLEM_URLS = {
    'BasicsOfInformation': "info.html",
    'TheDigitalAbstraction': "digital.html" ,
    'CMOSTechnology': "cmos.html",
    'GatesAndBooleanLogic': "gate.html",
    'SynthesisOfCombinationalLogic': "logic.html",
    'SequentialLogic': "sequential.html",
    'FSMs': "fsm.html",
    'SynchronizationAndMetastability': "synchronization.html",
    'Pipelining': "pipeline.html",
    'ModelsOfComputation': "computation.html",
    'ProgrammableMachines': "progmach.html",
    'MachineLanguage': "machinelang.html",
    'StacksAndProcedures': "procedures.html",
    'BuildingTheBeta': "beta.html",
    'MemoryHierarchy': "memhierarchy.html",
    'Caches': "caches.html",
    'VirtualMemory': "vm.html",
    'VirtualMachines': "os.html",
    'DevicesInterruptsAndRealTime': "realtime.html",
    'Semaphores': "semaphores.html",
    'PipelinedBeta': "pipelinedbeta.html",
    }

TOPIC_NUMBERS = {
    'BasicsOfInformation': 0,
    'TheDigitalAbstraction': 1,
    'CMOSTechnology': 2,
    'GatesAndBooleanLogic': 3,
    'SynthesisOfCombinationalLogic': 4,
    'SequentialLogic': 5,
    'FSMs': 6,
    'SynchronizationAndMetastability': 7,
    'Pipelining': 8,
    'ModelsOfComputation': 9,
    'ProgrammableMachines': 10,
    'MachineLanguage': 11,
    'StacksAndProcedures': 12,
    'BuildingTheBeta': 13,
    'MemoryHierarchy': 14,
    'Caches': 15,
    'VirtualMemory': 16,
    'VirtualMachines': 17,
    'DevicesInterruptsAndRealTime': 18,
    'Semaphores': 19,
    'PipelinedBeta': 20,
}


TOPIC_LIST = [
    'BasicsOfInformation',
    'TheDigitalAbstraction',
    'CMOSTechnology',
    'GatesAndBooleanLogic',
    'SynthesisOfCombinationalLogic',
    'SequentialLogic',
    'FSMs',
    'SynchronizationAndMetastability',
    'Pipelining',
    'ModelsOfComputation',
    'ProgrammableMachines',
    'MachineLanguage',
    'StacksAndProcedures',
    'BuildingTheBeta',
    'MemoryHierarchy',
    'Caches',
    'VirtualMemory',
    'VirtualMachines', 
    'DevicesInterruptsAndRealTime', 
    'Semaphores', 
    'PipelinedBeta',
]
