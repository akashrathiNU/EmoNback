/************************** 
 * Emonback_Practice *
 **************************/


// store info about the experiment session:
let expName = 'EmoNback_Practice';  // from the Builder filename that created this script
let expInfo = {
    'Please enter the Subject ID:': 'AANNNAAA',
    'Please enter the Session Number:': ["1", "2"],
    'Enter subject\'s handedness:': ["Right", "Left"],
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(TitlePageRoutineBegin());
flowScheduler.add(TitlePageRoutineEachFrame());
flowScheduler.add(TitlePageRoutineEnd());
flowScheduler.add(Instructions1RoutineBegin());
flowScheduler.add(Instructions1RoutineEachFrame());
flowScheduler.add(Instructions1RoutineEnd());
flowScheduler.add(Instructions2RoutineBegin());
flowScheduler.add(Instructions2RoutineEachFrame());
flowScheduler.add(Instructions2RoutineEnd());
flowScheduler.add(Instructions3RoutineBegin());
flowScheduler.add(Instructions3RoutineEachFrame());
flowScheduler.add(Instructions3RoutineEnd());
flowScheduler.add(Instructions5pt5RoutineBegin());
flowScheduler.add(Instructions5pt5RoutineEachFrame());
flowScheduler.add(Instructions5pt5RoutineEnd());
flowScheduler.add(Instructions6RoutineBegin());
flowScheduler.add(Instructions6RoutineEachFrame());
flowScheduler.add(Instructions6RoutineEnd());
flowScheduler.add(Instructions14RoutineBegin());
flowScheduler.add(Instructions14RoutineEachFrame());
flowScheduler.add(Instructions14RoutineEnd());
flowScheduler.add(Instructions6pt2RoutineBegin());
flowScheduler.add(Instructions6pt2RoutineEachFrame());
flowScheduler.add(Instructions6pt2RoutineEnd());
flowScheduler.add(PracticeTrial1_CueRoutineBegin());
flowScheduler.add(PracticeTrial1_CueRoutineEachFrame());
flowScheduler.add(PracticeTrial1_CueRoutineEnd());
const practiceLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practiceLoopLoopBegin(practiceLoopLoopScheduler));
flowScheduler.add(practiceLoopLoopScheduler);
flowScheduler.add(practiceLoopLoopEnd);



flowScheduler.add(InstructionsSpaceToContinueRoutineBegin());
flowScheduler.add(InstructionsSpaceToContinueRoutineEachFrame());
flowScheduler.add(InstructionsSpaceToContinueRoutineEnd());
flowScheduler.add(PracticeTrial2_CueRoutineBegin());
flowScheduler.add(PracticeTrial2_CueRoutineEachFrame());
flowScheduler.add(PracticeTrial2_CueRoutineEnd());
const practiceLoop2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practiceLoop2LoopBegin(practiceLoop2LoopScheduler));
flowScheduler.add(practiceLoop2LoopScheduler);
flowScheduler.add(practiceLoop2LoopEnd);



flowScheduler.add(InstructionsSpaceToContinueRoutineBegin());
flowScheduler.add(InstructionsSpaceToContinueRoutineEachFrame());
flowScheduler.add(InstructionsSpaceToContinueRoutineEnd());
flowScheduler.add(Instructions8RoutineBegin());
flowScheduler.add(Instructions8RoutineEachFrame());
flowScheduler.add(Instructions8RoutineEnd());
flowScheduler.add(Instructions11RoutineBegin());
flowScheduler.add(Instructions11RoutineEachFrame());
flowScheduler.add(Instructions11RoutineEnd());
flowScheduler.add(Instructions9RoutineBegin());
flowScheduler.add(Instructions9RoutineEachFrame());
flowScheduler.add(Instructions9RoutineEnd());
flowScheduler.add(Instructions21RoutineBegin());
flowScheduler.add(Instructions21RoutineEachFrame());
flowScheduler.add(Instructions21RoutineEnd());
flowScheduler.add(Instructions24RoutineBegin());
flowScheduler.add(Instructions24RoutineEachFrame());
flowScheduler.add(Instructions24RoutineEnd());
flowScheduler.add(Instructions25RoutineBegin());
flowScheduler.add(Instructions25RoutineEachFrame());
flowScheduler.add(Instructions25RoutineEnd());
flowScheduler.add(Instructions15RoutineBegin());
flowScheduler.add(Instructions15RoutineEachFrame());
flowScheduler.add(Instructions15RoutineEnd());
flowScheduler.add(Instructions32RoutineBegin());
flowScheduler.add(Instructions32RoutineEachFrame());
flowScheduler.add(Instructions32RoutineEnd());
flowScheduler.add(Instructions27RoutineBegin());
flowScheduler.add(Instructions27RoutineEachFrame());
flowScheduler.add(Instructions27RoutineEnd());
flowScheduler.add(Instructions33RoutineBegin());
flowScheduler.add(Instructions33RoutineEachFrame());
flowScheduler.add(Instructions33RoutineEnd());
flowScheduler.add(Instructions26RoutineBegin());
flowScheduler.add(Instructions26RoutineEachFrame());
flowScheduler.add(Instructions26RoutineEnd());
flowScheduler.add(Instructions34RoutineBegin());
flowScheduler.add(Instructions34RoutineEachFrame());
flowScheduler.add(Instructions34RoutineEnd());
flowScheduler.add(Instructions28RoutineBegin());
flowScheduler.add(Instructions28RoutineEachFrame());
flowScheduler.add(Instructions28RoutineEnd());
flowScheduler.add(Instructions29RoutineBegin());
flowScheduler.add(Instructions29RoutineEachFrame());
flowScheduler.add(Instructions29RoutineEnd());
flowScheduler.add(Instructions22RoutineBegin());
flowScheduler.add(Instructions22RoutineEachFrame());
flowScheduler.add(Instructions22RoutineEnd());
flowScheduler.add(Instructions30RoutineBegin());
flowScheduler.add(Instructions30RoutineEachFrame());
flowScheduler.add(Instructions30RoutineEnd());
const practiceLoop3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practiceLoop3LoopBegin(practiceLoop3LoopScheduler));
flowScheduler.add(practiceLoop3LoopScheduler);
flowScheduler.add(practiceLoop3LoopEnd);



flowScheduler.add(InstructionsSpaceToContinueRoutineBegin());
flowScheduler.add(InstructionsSpaceToContinueRoutineEachFrame());
flowScheduler.add(InstructionsSpaceToContinueRoutineEnd());
const practiceLoop4LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practiceLoop4LoopBegin(practiceLoop4LoopScheduler));
flowScheduler.add(practiceLoop4LoopScheduler);
flowScheduler.add(practiceLoop4LoopEnd);



flowScheduler.add(Instructions36RoutineBegin());
flowScheduler.add(Instructions36RoutineEachFrame());
flowScheduler.add(Instructions36RoutineEnd());
flowScheduler.add(PracticeTrial5_CueRoutineBegin());
flowScheduler.add(PracticeTrial5_CueRoutineEachFrame());
flowScheduler.add(PracticeTrial5_CueRoutineEnd());
const practiceLoop5LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practiceLoop5LoopBegin(practiceLoop5LoopScheduler));
flowScheduler.add(practiceLoop5LoopScheduler);
flowScheduler.add(practiceLoop5LoopEnd);



flowScheduler.add(PracticeTrial6_CueRoutineBegin());
flowScheduler.add(PracticeTrial6_CueRoutineEachFrame());
flowScheduler.add(PracticeTrial6_CueRoutineEnd());
const practiceLoop6LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practiceLoop6LoopBegin(practiceLoop6LoopScheduler));
flowScheduler.add(practiceLoop6LoopScheduler);
flowScheduler.add(practiceLoop6LoopEnd);



flowScheduler.add(PracticeTrial7_CueRoutineBegin());
flowScheduler.add(PracticeTrial7_CueRoutineEachFrame());
flowScheduler.add(PracticeTrial7_CueRoutineEnd());
const practiceLoop7LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practiceLoop7LoopBegin(practiceLoop7LoopScheduler));
flowScheduler.add(practiceLoop7LoopScheduler);
flowScheduler.add(practiceLoop7LoopEnd);



flowScheduler.add(PracticeTrial8_CueRoutineBegin());
flowScheduler.add(PracticeTrial8_CueRoutineEachFrame());
flowScheduler.add(PracticeTrial8_CueRoutineEnd());
const practiceLoop8LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practiceLoop8LoopBegin(practiceLoop8LoopScheduler));
flowScheduler.add(practiceLoop8LoopScheduler);
flowScheduler.add(practiceLoop8LoopEnd);



flowScheduler.add(GoodbyeRoutineBegin());
flowScheduler.add(GoodbyeRoutineEachFrame());
flowScheduler.add(GoodbyeRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'PracticeTrials1.xlsx', 'path': 'PracticeTrials1.xlsx'},
    {'name': 'VM Stimuli/PracticeNC2.bmp', 'path': 'VM Stimuli/PracticeNC2.bmp'},
    {'name': 'VM Stimuli/PracticeNC1.bmp', 'path': 'VM Stimuli/PracticeNC1.bmp'},
    {'name': 'VM Stimuli/PracticeNC3.bmp', 'path': 'VM Stimuli/PracticeNC3.bmp'},
    {'name': 'PracticeTrials2.xlsx', 'path': 'PracticeTrials2.xlsx'},
    {'name': 'VM Stimuli/Place1.bmp', 'path': 'VM Stimuli/Place1.bmp'},
    {'name': 'VM Stimuli/Place3.bmp', 'path': 'VM Stimuli/Place3.bmp'},
    {'name': 'VM Stimuli/Place5.bmp', 'path': 'VM Stimuli/Place5.bmp'},
    {'name': 'PracticeTrials3.xlsx', 'path': 'PracticeTrials3.xlsx'},
    {'name': 'VM Stimuli/PracticeFO2.bmp', 'path': 'VM Stimuli/PracticeFO2.bmp'},
    {'name': 'VM Stimuli/PracticeFO4.bmp', 'path': 'VM Stimuli/PracticeFO4.bmp'},
    {'name': 'VM Stimuli/PracticeFO1.bmp', 'path': 'VM Stimuli/PracticeFO1.bmp'},
    {'name': 'PracticeTrials4.xlsx', 'path': 'PracticeTrials4.xlsx'},
    {'name': 'VM Stimuli/Place1.bmp', 'path': 'VM Stimuli/Place1.bmp'},
    {'name': 'VM Stimuli/Place5.bmp', 'path': 'VM Stimuli/Place5.bmp'},
    {'name': 'VM Stimuli/Place6.bmp', 'path': 'VM Stimuli/Place6.bmp'},
    {'name': 'PracticeTrials5.xlsx', 'path': 'PracticeTrials5.xlsx'},
    {'name': 'VM Stimuli/PracticeHO1.bmp', 'path': 'VM Stimuli/PracticeHO1.bmp'},
    {'name': 'VM Stimuli/PracticeHO2.bmp', 'path': 'VM Stimuli/PracticeHO2.bmp'},
    {'name': 'VM Stimuli/PracticeHO3.bmp', 'path': 'VM Stimuli/PracticeHO3.bmp'},
    {'name': 'PracticeTrials6.xlsx', 'path': 'PracticeTrials6.xlsx'},
    {'name': 'VM Stimuli/Place5.bmp', 'path': 'VM Stimuli/Place5.bmp'},
    {'name': 'VM Stimuli/Place3.bmp', 'path': 'VM Stimuli/Place3.bmp'},
    {'name': 'VM Stimuli/Place6.bmp', 'path': 'VM Stimuli/Place6.bmp'},
    {'name': 'PracticeTrials7.xlsx', 'path': 'PracticeTrials7.xlsx'},
    {'name': 'VM Stimuli/Place3.bmp', 'path': 'VM Stimuli/Place3.bmp'},
    {'name': 'VM Stimuli/Place5.bmp', 'path': 'VM Stimuli/Place5.bmp'},
    {'name': 'VM Stimuli/Place1.bmp', 'path': 'VM Stimuli/Place1.bmp'},
    {'name': 'PracticeTrials8.xlsx', 'path': 'PracticeTrials8.xlsx'},
    {'name': 'VM Stimuli/PracticeNC1.bmp', 'path': 'VM Stimuli/PracticeNC1.bmp'},
    {'name': 'VM Stimuli/PracticeNC2.bmp', 'path': 'VM Stimuli/PracticeNC2.bmp'},
    {'name': 'VM Stimuli/PracticeNC3.bmp', 'path': 'VM Stimuli/PracticeNC3.bmp'},
    {'name': 'VM Stimuli/PracticeNC1.bmp', 'path': 'VM Stimuli/PracticeNC1.bmp'},
    {'name': 'VM Stimuli/Place1.bmp', 'path': 'VM Stimuli/Place1.bmp'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': 'VM Stimuli/PracticeFO1.bmp', 'path': 'VM Stimuli/PracticeFO1.bmp'},
    {'name': 'VM Stimuli/PracticeFO2.bmp', 'path': 'VM Stimuli/PracticeFO2.bmp'},
    {'name': 'VM Stimuli/PracticeFO3.bmp', 'path': 'VM Stimuli/PracticeFO3.bmp'},
    {'name': 'VM Stimuli/Place3.bmp', 'path': 'VM Stimuli/Place3.bmp'},
    {'name': 'VM Stimuli/PracticeNC2.bmp', 'path': 'VM Stimuli/PracticeNC2.bmp'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2025.2.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["Please enter the Subject ID:"]}_${expInfo["Please enter the Session Number:"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var TitlePageClock;
var NextPage;
var NbackTitle;
var matchKey;
var noMatchKey;
var Instructions1Clock;
var NextPage_2;
var Instructions_1;
var Instructions2Clock;
var NextPage_3;
var Instructions_2;
var FaceImage;
var Instructions3Clock;
var NextPage_4;
var Instructions_3;
var PlaceImage;
var Instructions5pt5Clock;
var NextPage_5;
var Instructions_5pt5;
var Instructions6Clock;
var NextPage_6;
var Instructions_6;
var Instructions_6_Target;
var TargetImage;
var Instructions_6_Match;
var Instructions14Clock;
var NextPage_7;
var Instructions_14;
var Instructions6pt2Clock;
var NextPage_8;
var Instructions_6pt2;
var PracticeTrial1_CueClock;
var CueFix_1;
var CueTarget_1;
var CueTargetImage_1;
var PracticeTrial_StimClock;
var response;
var Stim;
var Stim_Match;
var Stim_No_Match;
var PracticeTrial_FeedbackClock;
var Fix;
var Feedback;
var InstructionsSpaceToContinueClock;
var NextPage_9;
var Instructions_Space;
var PracticeTrial2_CueClock;
var CueFix_2;
var CueTarget_2;
var CueTargetImage_2;
var Instructions8Clock;
var NextPage_10;
var Instructions_8;
var Instructions11Clock;
var NextPage_11;
var Instructions_11;
var Instructions9Clock;
var NextPage_12;
var Instructions_9;
var Example_Stim;
var Example_Match;
var Example_No_Match;
var Instructions21Clock;
var NextPage_13;
var Instructions_21;
var One_Back_Example_Stim;
var Example_Stim_2;
var Example_Match_2;
var Example_No_Match_2;
var Instructions24Clock;
var NextPage_14;
var Instructions_24;
var Green_Border;
var Two_Back_Example_Stim;
var One_Back_Example_Stim_2;
var Example_Stim_3;
var Example_Match_3;
var Example_No_Match_3;
var Instructions25Clock;
var NextPage_15;
var Instructions_25;
var Two_Back_Example_Stim_2;
var One_Back_Example_Stim_3;
var Example_Stim_4;
var Example_Match_4;
var Example_No_Match_4;
var Instructions15Clock;
var NextPage_16;
var Instructions_15;
var Instructions32Clock;
var NextPage_17;
var Instructions_32;
var Example_Stim_5;
var Example_Stim_Match_3;
var Example_Stim_No_Match_3;
var Instructions27Clock;
var NextPage_18;
var Instructions_27;
var Example_Stim_6;
var Example_Stim_Match;
var Example_Stim_No_Match;
var Instructions33Clock;
var NextPage_19;
var Instructions_33;
var Example_Stim_7;
var Example_Stim_Match_4;
var Example_Stim_No_Match_4;
var Instructions26Clock;
var NextPage_20;
var Instructions_26;
var One_Back_Example_Stim_4;
var Example_Stim_8;
var Example_Stim_Match_2;
var Example_Stim_No_Match_2;
var Instructions34Clock;
var NextPage_21;
var Instructions;
var Example_Stim_9;
var Example_Stim_Match_5;
var Example_Stim_No_Match_5;
var Instructions28Clock;
var NextPage_22;
var Instructions_28;
var Two_Back_Example_Stim_3;
var One_Back_Example_Stim_5;
var Example_Stim_10;
var Example_Stim_Match_6;
var Example_Stim_No_Match_6;
var Instructions29Clock;
var NextPage_23;
var Instructions_29;
var Green_Border_2;
var Two_Back_Example_Stim_4;
var One_Back_Example_Stim_6;
var Example_Stim_11;
var Example_Stim_Match_7;
var Example_Stim_No_Match_7;
var Instructions22Clock;
var NextPage_24;
var Instructions_22;
var Instructions30Clock;
var NextPage_25;
var Instructions_30;
var Instructions36Clock;
var NextPage_26;
var Instructions_36;
var PracticeTrial5_CueClock;
var CueFix_5;
var Cue_2Back;
var PracticeTrial6_CueClock;
var CueFix_6;
var CueTarget_6;
var CueTargetImage_6;
var PracticeTrial7_CueClock;
var CueFix_7;
var Cue_2Back_2;
var PracticeTrial8_CueClock;
var CueFix_8;
var CueTarget_8;
var CueTargetImage_8;
var GoodbyeClock;
var EndProgram;
var AllDone;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "TitlePage"
  TitlePageClock = new util.Clock();
  NextPage = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  NbackTitle = new visual.TextBox({
    win: psychoJS.window,
    name: 'NbackTitle',
    text: 'N-back',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Run 'Begin Experiment' code from handnessLogic
  if ((expInfo["handedness"].toLowerCase() === "right")) {
      matchKey = "left";
      noMatchKey = "right";
  } else {
      matchKey = "right";
      noMatchKey = "left";
  }
  
  // Initialize components for Routine "Instructions1"
  Instructions1Clock = new util.Clock();
  NextPage_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_1 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_1',
    text: 'In this game, you will see different pictures. \nThese pictures will be...',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Initialize components for Routine "Instructions2"
  Instructions2Clock = new util.Clock();
  NextPage_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_2',
    text: 'Faces',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0.25], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  FaceImage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'FaceImage', units : undefined, 
    image : 'VM Stimuli/PracticeNC1.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "Instructions3"
  Instructions3Clock = new util.Clock();
  NextPage_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_3 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_3',
    text: 'Places',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0.25], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  PlaceImage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'PlaceImage', units : undefined, 
    image : 'VM Stimuli/Place1.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "Instructions5pt5"
  Instructions5pt5Clock = new util.Clock();
  NextPage_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_5pt5 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_5pt5',
    text: 'You will play two different games with these pictures:\n0-Back and 2-Back.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Initialize components for Routine "Instructions6"
  Instructions6Clock = new util.Clock();
  NextPage_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_6 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_6',
    text: 'At the beginning of 0-Back, you will see a target picture. Then, \npictures will appear one at a time. Decide if each picture \nmatches the target. For example, if you see:',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0.25], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  Instructions_6_Target = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_6_Target',
    text: 'Target          =',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [(- 0.1), 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -2.0 
  });
  
  TargetImage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'TargetImage', units : undefined, 
    image : 'VM Stimuli/PracticeNC1.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.2, 0], 
    draggable: false,
    size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  Instructions_6_Match = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_6_Match',
    text: 'Press MATCH with your POINTER finger \nevery time you see that picture. Please press it now.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, (- 0.25)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -4.0 
  });
  
  // Initialize components for Routine "Instructions14"
  Instructions14Clock = new util.Clock();
  NextPage_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_14 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_14',
    text: 'Press NO MATCH with your MIDDLE finger for \nevery picture that is different than the target. \n\nPlease press it now.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Initialize components for Routine "Instructions6pt2"
  Instructions6pt2Clock = new util.Clock();
  NextPage_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_6pt2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_6pt2',
    text: "Let's practice now!",
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Initialize components for Routine "PracticeTrial1_Cue"
  PracticeTrial1_CueClock = new util.Clock();
  CueFix_1 = new visual.TextBox({
    win: psychoJS.window,
    name: 'CueFix_1',
    text: '+',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: (1.0000, -1.0000, 1.0000), colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  CueTarget_1 = new visual.TextBox({
    win: psychoJS.window,
    name: 'CueTarget_1',
    text: 'Target          =',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [(- 0.15), 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  CueTargetImage_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'CueTargetImage_1', units : undefined, 
    image : 'VM Stimuli/PracticeNC1.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.15, 0], 
    draggable: false,
    size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "PracticeTrial_Stim"
  PracticeTrial_StimClock = new util.Clock();
  response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Stim = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Stim', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  Stim_Match = new visual.TextBox({
    win: psychoJS.window,
    name: 'Stim_Match',
    text: 'MATCH\nPOINTER',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [(- 0.2), (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -3.0 
  });
  
  Stim_No_Match = new visual.TextBox({
    win: psychoJS.window,
    name: 'Stim_No_Match',
    text: 'NO MATCH\nMIDDLE',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0.2, (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -4.0 
  });
  
  // Initialize components for Routine "PracticeTrial_Feedback"
  PracticeTrial_FeedbackClock = new util.Clock();
  Fix = new visual.TextBox({
    win: psychoJS.window,
    name: 'Fix',
    text: '+',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  Feedback = new visual.TextBox({
    win: psychoJS.window,
    name: 'Feedback',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Initialize components for Routine "InstructionsSpaceToContinue"
  InstructionsSpaceToContinueClock = new util.Clock();
  NextPage_9 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_Space = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_Space',
    text: 'Press SPACE to continue',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Initialize components for Routine "PracticeTrial2_Cue"
  PracticeTrial2_CueClock = new util.Clock();
  CueFix_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'CueFix_2',
    text: '+',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: (1.0000, -1.0000, 1.0000), colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  CueTarget_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'CueTarget_2',
    text: 'Target          =',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [(- 0.15), 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  CueTargetImage_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'CueTargetImage_2', units : undefined, 
    image : 'VM Stimuli/Place1.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.15, 0], 
    draggable: false,
    size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "Instructions8"
  Instructions8Clock = new util.Clock();
  NextPage_10 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_8 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_8',
    text: 'For 2-Back, you will see pictures one at a time on the screen.\n\nFor each picture, decide if it is the same as the one two pictures back. ',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Initialize components for Routine "Instructions11"
  Instructions11Clock = new util.Clock();
  NextPage_11 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_11 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_11',
    text: 'If it is the same, press MATCH with your POINTER finger. \nOtherwise, NO MATCH with your MIDDLE finger. \n\n\nHere is an example:\n',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Initialize components for Routine "Instructions9"
  Instructions9Clock = new util.Clock();
  NextPage_12 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_9 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_9',
    text: 'This is a NO MATCH because nothing was shown two back.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0.2], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  Example_Stim = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Example_Stim', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  Example_Match = new visual.TextBox({
    win: psychoJS.window,
    name: 'Example_Match',
    text: 'MATCH\nPOINTER',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [(- 0.2), (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -3.0 
  });
  
  Example_No_Match = new visual.TextBox({
    win: psychoJS.window,
    name: 'Example_No_Match',
    text: 'NO MATCH\nMIDDLE',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0.2, (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'limegreen', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -4.0 
  });
  
  // Initialize components for Routine "Instructions21"
  Instructions21Clock = new util.Clock();
  NextPage_13 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_21 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_21',
    text: 'Again, this is a NO MATCH because nothing was shown two back.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0.2], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  One_Back_Example_Stim = new visual.ImageStim({
    win : psychoJS.window,
    name : 'One_Back_Example_Stim', units : undefined, 
    image : 'VM Stimuli/PracticeFO1.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.3), 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  Example_Stim_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Example_Stim_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  Example_Match_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Example_Match_2',
    text: 'MATCH\nPOINTER',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [(- 0.2), (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -4.0 
  });
  
  Example_No_Match_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Example_No_Match_2',
    text: 'NO MATCH\nMIDDLE',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0.2, (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'limegreen', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -5.0 
  });
  
  // Initialize components for Routine "Instructions24"
  Instructions24Clock = new util.Clock();
  NextPage_14 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_24 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_24',
    text: 'This is a MATCH because it is the same as the picture shown two back.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0.2], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  Green_Border = new visual.Rect ({
    win: psychoJS.window, name: 'Green_Border', 
    width: [0.15, 0.15][0], height: [0.15, 0.15][1],
    ori: 0.0, 
    pos: [(- 0.5), 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('limegreen'), 
    fillColor: new util.Color('limegreen'), 
    colorSpace: 'rgb', 
    opacity: 1.0, 
    depth: -2, 
    interpolate: true, 
  });
  
  Two_Back_Example_Stim = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Two_Back_Example_Stim', units : undefined, 
    image : 'VM Stimuli/PracticeFO1.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.5), 0], 
    draggable: false,
    size : [0.13, 0.13],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  One_Back_Example_Stim_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'One_Back_Example_Stim_2', units : undefined, 
    image : 'VM Stimuli/PracticeFO2.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.3), 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  Example_Stim_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Example_Stim_3', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  Example_Match_3 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Example_Match_3',
    text: 'MATCH\nPOINTER',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [(- 0.2), (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'limegreen', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -6.0 
  });
  
  Example_No_Match_3 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Example_No_Match_3',
    text: 'NO MATCH\nMIDDLE',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0.2, (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -7.0 
  });
  
  // Initialize components for Routine "Instructions25"
  Instructions25Clock = new util.Clock();
  NextPage_15 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_25 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_25',
    text: 'This is a NO MATCH because a different picture was shown two back.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0.2], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  Two_Back_Example_Stim_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Two_Back_Example_Stim_2', units : undefined, 
    image : 'VM Stimuli/PracticeFO2.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.5), 0], 
    draggable: false,
    size : [0.13, 0.13],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  One_Back_Example_Stim_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'One_Back_Example_Stim_3', units : undefined, 
    image : 'VM Stimuli/PracticeFO1.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.3), 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  Example_Stim_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Example_Stim_4', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  Example_Match_4 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Example_Match_4',
    text: 'MATCH\nPOINTER',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [(- 0.2), (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -5.0 
  });
  
  Example_No_Match_4 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Example_No_Match_4',
    text: 'NO MATCH\nMIDDLE',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0.2, (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'limegreen', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -6.0 
  });
  
  // Initialize components for Routine "Instructions15"
  Instructions15Clock = new util.Clock();
  NextPage_16 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_15 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_15',
    text: "Let's try one together!",
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Initialize components for Routine "Instructions32"
  Instructions32Clock = new util.Clock();
  NextPage_17 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_32 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_32',
    text: 'MATCH or NO MATCH?',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0.2], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  Example_Stim_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Example_Stim_5', units : undefined, 
    image : 'VM Stimuli/PracticeFO2.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  Example_Stim_Match_3 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Example_Stim_Match_3',
    text: 'MATCH\nPOINTER',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [(- 0.2), (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -3.0 
  });
  
  Example_Stim_No_Match_3 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Example_Stim_No_Match_3',
    text: 'NO MATCH\nMIDDLE',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0.2, (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -4.0 
  });
  
  // Initialize components for Routine "Instructions27"
  Instructions27Clock = new util.Clock();
  NextPage_18 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_27 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_27',
    text: 'This is a NO MATCH because nothing was shown two back.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0.2], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  Example_Stim_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Example_Stim_6', units : undefined, 
    image : 'VM Stimuli/PracticeFO2.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  Example_Stim_Match = new visual.TextBox({
    win: psychoJS.window,
    name: 'Example_Stim_Match',
    text: 'MATCH\nPOINTER',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [(- 0.2), (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -3.0 
  });
  
  Example_Stim_No_Match = new visual.TextBox({
    win: psychoJS.window,
    name: 'Example_Stim_No_Match',
    text: 'NO MATCH\nMIDDLE',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0.2, (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'limegreen', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -4.0 
  });
  
  // Initialize components for Routine "Instructions33"
  Instructions33Clock = new util.Clock();
  NextPage_19 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_33 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_33',
    text: 'MATCH or NO MATCH?',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0.2], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  Example_Stim_7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Example_Stim_7', units : undefined, 
    image : 'VM Stimuli/PracticeFO3.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  Example_Stim_Match_4 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Example_Stim_Match_4',
    text: 'MATCH\nPOINTER',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [(- 0.2), (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -3.0 
  });
  
  Example_Stim_No_Match_4 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Example_Stim_No_Match_4',
    text: 'NO MATCH\nMIDDLE',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0.2, (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -4.0 
  });
  
  // Initialize components for Routine "Instructions26"
  Instructions26Clock = new util.Clock();
  NextPage_20 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_26 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_26',
    text: 'Again, this is a NO MATCH because nothing was shown two back.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0.2], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  One_Back_Example_Stim_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'One_Back_Example_Stim_4', units : undefined, 
    image : 'VM Stimuli/PracticeFO2.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.3), 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  Example_Stim_8 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Example_Stim_8', units : undefined, 
    image : 'VM Stimuli/PracticeFO3.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  Example_Stim_Match_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Example_Stim_Match_2',
    text: 'MATCH\nPOINTER',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [(- 0.2), (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -4.0 
  });
  
  Example_Stim_No_Match_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Example_Stim_No_Match_2',
    text: 'NO MATCH\nMIDDLE',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0.2, (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'limegreen', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -5.0 
  });
  
  // Initialize components for Routine "Instructions34"
  Instructions34Clock = new util.Clock();
  NextPage_21 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions',
    text: 'MATCH or NO MATCH?',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0.2], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  Example_Stim_9 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Example_Stim_9', units : undefined, 
    image : 'VM Stimuli/PracticeFO1.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  Example_Stim_Match_5 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Example_Stim_Match_5',
    text: 'MATCH\nPOINTER',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [(- 0.2), (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -3.0 
  });
  
  Example_Stim_No_Match_5 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Example_Stim_No_Match_5',
    text: 'NO MATCH\nMIDDLE',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0.2, (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -4.0 
  });
  
  // Initialize components for Routine "Instructions28"
  Instructions28Clock = new util.Clock();
  NextPage_22 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_28 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_28',
    text: 'This is a NO MATCH because this picture is different from the one that was presented two back.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0.2], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  Two_Back_Example_Stim_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Two_Back_Example_Stim_3', units : undefined, 
    image : 'VM Stimuli/PracticeFO2.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.5), 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  One_Back_Example_Stim_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'One_Back_Example_Stim_5', units : undefined, 
    image : 'VM Stimuli/PracticeFO3.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.3), 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  Example_Stim_10 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Example_Stim_10', units : undefined, 
    image : 'VM Stimuli/PracticeFO1.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  Example_Stim_Match_6 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Example_Stim_Match_6',
    text: 'MATCH\nPOINTER',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [(- 0.2), (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -5.0 
  });
  
  Example_Stim_No_Match_6 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Example_Stim_No_Match_6',
    text: 'NO MATCH\nMIDDLE',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0.2, (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'limegreen', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -6.0 
  });
  
  // Initialize components for Routine "Instructions29"
  Instructions29Clock = new util.Clock();
  NextPage_23 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_29 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_29',
    text: 'Remember a MATCH is only when the same picture was presented two back.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0.2], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  Green_Border_2 = new visual.Rect ({
    win: psychoJS.window, name: 'Green_Border_2', 
    width: [0.15, 0.15][0], height: [0.15, 0.15][1],
    ori: 0.0, 
    pos: [(- 0.5), 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('limegreen'), 
    fillColor: new util.Color('limegreen'), 
    colorSpace: 'rgb', 
    opacity: 1.0, 
    depth: -2, 
    interpolate: true, 
  });
  
  Two_Back_Example_Stim_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Two_Back_Example_Stim_4', units : undefined, 
    image : 'VM Stimuli/PracticeFO3.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.5), 0], 
    draggable: false,
    size : [0.13, 0.13],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  One_Back_Example_Stim_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'One_Back_Example_Stim_6', units : undefined, 
    image : 'VM Stimuli/PracticeFO1.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.3), 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  Example_Stim_11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Example_Stim_11', units : undefined, 
    image : 'VM Stimuli/PracticeFO3.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  Example_Stim_Match_7 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Example_Stim_Match_7',
    text: 'MATCH\nPOINTER',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [(- 0.2), (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'limegreen', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -6.0 
  });
  
  Example_Stim_No_Match_7 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Example_Stim_No_Match_7',
    text: 'NO MATCH\nMIDDLE',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0.2, (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -7.0 
  });
  
  // Initialize components for Routine "Instructions22"
  Instructions22Clock = new util.Clock();
  NextPage_24 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_22 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_22',
    text: 'In the game you will see pictures one at a time. \nYou need to remember what was shown two back.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Initialize components for Routine "Instructions30"
  Instructions30Clock = new util.Clock();
  NextPage_25 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_30 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_30',
    text: "Let's practice!",
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Initialize components for Routine "Instructions36"
  Instructions36Clock = new util.Clock();
  NextPage_26 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Instructions_36 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Instructions_36',
    text: "Now let's practice switching between the two games.  The plus sign will turn purple before the games switch.\n\nMake sure you pay attention to see if the game is the 0-back or 2-back!",
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Initialize components for Routine "PracticeTrial5_Cue"
  PracticeTrial5_CueClock = new util.Clock();
  CueFix_5 = new visual.TextBox({
    win: psychoJS.window,
    name: 'CueFix_5',
    text: '+',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: (1.0000, -1.0000, 1.0000), colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  Cue_2Back = new visual.TextBox({
    win: psychoJS.window,
    name: 'Cue_2Back',
    text: '2-Back',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Initialize components for Routine "PracticeTrial6_Cue"
  PracticeTrial6_CueClock = new util.Clock();
  CueFix_6 = new visual.TextBox({
    win: psychoJS.window,
    name: 'CueFix_6',
    text: '+',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: (1.0000, -1.0000, 1.0000), colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  CueTarget_6 = new visual.TextBox({
    win: psychoJS.window,
    name: 'CueTarget_6',
    text: 'Target          =',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [(- 0.15), 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  CueTargetImage_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'CueTargetImage_6', units : undefined, 
    image : 'VM Stimuli/Place3.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.15, 0], 
    draggable: false,
    size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "PracticeTrial7_Cue"
  PracticeTrial7_CueClock = new util.Clock();
  CueFix_7 = new visual.TextBox({
    win: psychoJS.window,
    name: 'CueFix_7',
    text: '+',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: (1.0000, -1.0000, 1.0000), colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  Cue_2Back_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'Cue_2Back_2',
    text: '2-Back',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Initialize components for Routine "PracticeTrial8_Cue"
  PracticeTrial8_CueClock = new util.Clock();
  CueFix_8 = new visual.TextBox({
    win: psychoJS.window,
    name: 'CueFix_8',
    text: '+',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: (1.0000, -1.0000, 1.0000), colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  CueTarget_8 = new visual.TextBox({
    win: psychoJS.window,
    name: 'CueTarget_8',
    text: 'Target          =',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [(- 0.15), 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  CueTargetImage_8 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'CueTargetImage_8', units : undefined, 
    image : 'VM Stimuli/PracticeNC2.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.15, 0], 
    draggable: false,
    size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "Goodbye"
  GoodbyeClock = new util.Clock();
  EndProgram = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  AllDone = new visual.TextBox({
    win: psychoJS.window,
    name: 'AllDone',
    text: 'All Done!\n\n\nPlease tell the experimenter you are finished.\n\n\nPress the SPACEBAR to exit.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -2.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var TitlePageMaxDurationReached;
var _NextPage_allKeys;
var TitlePageMaxDuration;
var TitlePageComponents;
function TitlePageRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'TitlePage' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    TitlePageClock.reset();
    routineTimer.reset();
    TitlePageMaxDurationReached = false;
    // update component parameters for each repeat
    NextPage.keys = undefined;
    NextPage.rt = undefined;
    _NextPage_allKeys = [];
    psychoJS.experiment.addData('TitlePage.started', globalClock.getTime());
    TitlePageMaxDuration = null
    // keep track of which components have finished
    TitlePageComponents = [];
    TitlePageComponents.push(NextPage);
    TitlePageComponents.push(NbackTitle);
    
    TitlePageComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function TitlePageRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'TitlePage' ---
    // get current time
    t = TitlePageClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *NextPage* updates
    if (t >= 0.0 && NextPage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      NextPage.tStart = t;  // (not accounting for frame time here)
      NextPage.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { NextPage.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { NextPage.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { NextPage.clearEvents(); });
    }
    
    // if NextPage is active this frame...
    if (NextPage.status === PsychoJS.Status.STARTED) {
      let theseKeys = NextPage.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _NextPage_allKeys = _NextPage_allKeys.concat(theseKeys);
      if (_NextPage_allKeys.length > 0) {
        NextPage.keys = _NextPage_allKeys[_NextPage_allKeys.length - 1].name;  // just the last key pressed
        NextPage.rt = _NextPage_allKeys[_NextPage_allKeys.length - 1].rt;
        NextPage.duration = _NextPage_allKeys[_NextPage_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *NbackTitle* updates
    if (t >= 0.0 && NbackTitle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      NbackTitle.tStart = t;  // (not accounting for frame time here)
      NbackTitle.frameNStart = frameN;  // exact frame index
      
      NbackTitle.setAutoDraw(true);
    }
    
    
    // if NbackTitle is active this frame...
    if (NbackTitle.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    TitlePageComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TitlePageRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'TitlePage' ---
    TitlePageComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('TitlePage.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(NextPage.corr, level);
    }
    psychoJS.experiment.addData('NextPage.keys', NextPage.keys);
    if (typeof NextPage.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('NextPage.rt', NextPage.rt);
        psychoJS.experiment.addData('NextPage.duration', NextPage.duration);
        routineTimer.reset();
        }
    
    NextPage.stop();
    // the Routine "TitlePage" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Instructions1MaxDurationReached;
var _NextPage_2_allKeys;
var Instructions1MaxDuration;
var Instructions1Components;
function Instructions1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instructions1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    Instructions1Clock.reset();
    routineTimer.reset();
    Instructions1MaxDurationReached = false;
    // update component parameters for each repeat
    NextPage_2.keys = undefined;
    NextPage_2.rt = undefined;
    _NextPage_2_allKeys = [];
    psychoJS.experiment.addData('Instructions1.started', globalClock.getTime());
    Instructions1MaxDuration = null
    // keep track of which components have finished
    Instructions1Components = [];
    Instructions1Components.push(NextPage_2);
    Instructions1Components.push(Instructions_1);
    
    Instructions1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Instructions1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instructions1' ---
    // get current time
    t = Instructions1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *NextPage_2* updates
    if (t >= 0.0 && NextPage_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      NextPage_2.tStart = t;  // (not accounting for frame time here)
      NextPage_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { NextPage_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { NextPage_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { NextPage_2.clearEvents(); });
    }
    
    // if NextPage_2 is active this frame...
    if (NextPage_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = NextPage_2.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _NextPage_2_allKeys = _NextPage_2_allKeys.concat(theseKeys);
      if (_NextPage_2_allKeys.length > 0) {
        NextPage_2.keys = _NextPage_2_allKeys[_NextPage_2_allKeys.length - 1].name;  // just the last key pressed
        NextPage_2.rt = _NextPage_2_allKeys[_NextPage_2_allKeys.length - 1].rt;
        NextPage_2.duration = _NextPage_2_allKeys[_NextPage_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Instructions_1* updates
    if (t >= 0.0 && Instructions_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instructions_1.tStart = t;  // (not accounting for frame time here)
      Instructions_1.frameNStart = frameN;  // exact frame index
      
      Instructions_1.setAutoDraw(true);
    }
    
    
    // if Instructions_1 is active this frame...
    if (Instructions_1.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Instructions1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instructions1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instructions1' ---
    Instructions1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Instructions1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(NextPage_2.corr, level);
    }
    psychoJS.experiment.addData('NextPage_2.keys', NextPage_2.keys);
    if (typeof NextPage_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('NextPage_2.rt', NextPage_2.rt);
        psychoJS.experiment.addData('NextPage_2.duration', NextPage_2.duration);
        routineTimer.reset();
        }
    
    NextPage_2.stop();
    // the Routine "Instructions1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Instructions2MaxDurationReached;
var _NextPage_3_allKeys;
var Instructions2MaxDuration;
var Instructions2Components;
function Instructions2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instructions2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    Instructions2Clock.reset();
    routineTimer.reset();
    Instructions2MaxDurationReached = false;
    // update component parameters for each repeat
    NextPage_3.keys = undefined;
    NextPage_3.rt = undefined;
    _NextPage_3_allKeys = [];
    psychoJS.experiment.addData('Instructions2.started', globalClock.getTime());
    Instructions2MaxDuration = null
    // keep track of which components have finished
    Instructions2Components = [];
    Instructions2Components.push(NextPage_3);
    Instructions2Components.push(Instructions_2);
    Instructions2Components.push(FaceImage);
    
    Instructions2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Instructions2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instructions2' ---
    // get current time
    t = Instructions2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *NextPage_3* updates
    if (t >= 0.0 && NextPage_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      NextPage_3.tStart = t;  // (not accounting for frame time here)
      NextPage_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { NextPage_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { NextPage_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { NextPage_3.clearEvents(); });
    }
    
    // if NextPage_3 is active this frame...
    if (NextPage_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = NextPage_3.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _NextPage_3_allKeys = _NextPage_3_allKeys.concat(theseKeys);
      if (_NextPage_3_allKeys.length > 0) {
        NextPage_3.keys = _NextPage_3_allKeys[_NextPage_3_allKeys.length - 1].name;  // just the last key pressed
        NextPage_3.rt = _NextPage_3_allKeys[_NextPage_3_allKeys.length - 1].rt;
        NextPage_3.duration = _NextPage_3_allKeys[_NextPage_3_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Instructions_2* updates
    if (t >= 0.0 && Instructions_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instructions_2.tStart = t;  // (not accounting for frame time here)
      Instructions_2.frameNStart = frameN;  // exact frame index
      
      Instructions_2.setAutoDraw(true);
    }
    
    
    // if Instructions_2 is active this frame...
    if (Instructions_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *FaceImage* updates
    if (t >= 0.0 && FaceImage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      FaceImage.tStart = t;  // (not accounting for frame time here)
      FaceImage.frameNStart = frameN;  // exact frame index
      
      FaceImage.setAutoDraw(true);
    }
    
    
    // if FaceImage is active this frame...
    if (FaceImage.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Instructions2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instructions2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instructions2' ---
    Instructions2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Instructions2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(NextPage_3.corr, level);
    }
    psychoJS.experiment.addData('NextPage_3.keys', NextPage_3.keys);
    if (typeof NextPage_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('NextPage_3.rt', NextPage_3.rt);
        psychoJS.experiment.addData('NextPage_3.duration', NextPage_3.duration);
        routineTimer.reset();
        }
    
    NextPage_3.stop();
    // the Routine "Instructions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Instructions3MaxDurationReached;
var _NextPage_4_allKeys;
var Instructions3MaxDuration;
var Instructions3Components;
function Instructions3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instructions3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    Instructions3Clock.reset();
    routineTimer.reset();
    Instructions3MaxDurationReached = false;
    // update component parameters for each repeat
    NextPage_4.keys = undefined;
    NextPage_4.rt = undefined;
    _NextPage_4_allKeys = [];
    psychoJS.experiment.addData('Instructions3.started', globalClock.getTime());
    Instructions3MaxDuration = null
    // keep track of which components have finished
    Instructions3Components = [];
    Instructions3Components.push(NextPage_4);
    Instructions3Components.push(Instructions_3);
    Instructions3Components.push(PlaceImage);
    
    Instructions3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Instructions3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instructions3' ---
    // get current time
    t = Instructions3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *NextPage_4* updates
    if (t >= 0.0 && NextPage_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      NextPage_4.tStart = t;  // (not accounting for frame time here)
      NextPage_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { NextPage_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { NextPage_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { NextPage_4.clearEvents(); });
    }
    
    // if NextPage_4 is active this frame...
    if (NextPage_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = NextPage_4.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _NextPage_4_allKeys = _NextPage_4_allKeys.concat(theseKeys);
      if (_NextPage_4_allKeys.length > 0) {
        NextPage_4.keys = _NextPage_4_allKeys[_NextPage_4_allKeys.length - 1].name;  // just the last key pressed
        NextPage_4.rt = _NextPage_4_allKeys[_NextPage_4_allKeys.length - 1].rt;
        NextPage_4.duration = _NextPage_4_allKeys[_NextPage_4_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Instructions_3* updates
    if (t >= 0.0 && Instructions_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instructions_3.tStart = t;  // (not accounting for frame time here)
      Instructions_3.frameNStart = frameN;  // exact frame index
      
      Instructions_3.setAutoDraw(true);
    }
    
    
    // if Instructions_3 is active this frame...
    if (Instructions_3.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *PlaceImage* updates
    if (t >= 0.0 && PlaceImage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PlaceImage.tStart = t;  // (not accounting for frame time here)
      PlaceImage.frameNStart = frameN;  // exact frame index
      
      PlaceImage.setAutoDraw(true);
    }
    
    
    // if PlaceImage is active this frame...
    if (PlaceImage.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Instructions3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instructions3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instructions3' ---
    Instructions3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Instructions3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(NextPage_4.corr, level);
    }
    psychoJS.experiment.addData('NextPage_4.keys', NextPage_4.keys);
    if (typeof NextPage_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('NextPage_4.rt', NextPage_4.rt);
        psychoJS.experiment.addData('NextPage_4.duration', NextPage_4.duration);
        routineTimer.reset();
        }
    
    NextPage_4.stop();
    // the Routine "Instructions3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Instructions5pt5MaxDurationReached;
var _NextPage_5_allKeys;
var Instructions5pt5MaxDuration;
var Instructions5pt5Components;
function Instructions5pt5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instructions5pt5' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    Instructions5pt5Clock.reset();
    routineTimer.reset();
    Instructions5pt5MaxDurationReached = false;
    // update component parameters for each repeat
    NextPage_5.keys = undefined;
    NextPage_5.rt = undefined;
    _NextPage_5_allKeys = [];
    psychoJS.experiment.addData('Instructions5pt5.started', globalClock.getTime());
    Instructions5pt5MaxDuration = null
    // keep track of which components have finished
    Instructions5pt5Components = [];
    Instructions5pt5Components.push(NextPage_5);
    Instructions5pt5Components.push(Instructions_5pt5);
    
    Instructions5pt5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Instructions5pt5RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instructions5pt5' ---
    // get current time
    t = Instructions5pt5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *NextPage_5* updates
    if (t >= 0.0 && NextPage_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      NextPage_5.tStart = t;  // (not accounting for frame time here)
      NextPage_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { NextPage_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { NextPage_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { NextPage_5.clearEvents(); });
    }
    
    // if NextPage_5 is active this frame...
    if (NextPage_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = NextPage_5.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _NextPage_5_allKeys = _NextPage_5_allKeys.concat(theseKeys);
      if (_NextPage_5_allKeys.length > 0) {
        NextPage_5.keys = _NextPage_5_allKeys[_NextPage_5_allKeys.length - 1].name;  // just the last key pressed
        NextPage_5.rt = _NextPage_5_allKeys[_NextPage_5_allKeys.length - 1].rt;
        NextPage_5.duration = _NextPage_5_allKeys[_NextPage_5_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Instructions_5pt5* updates
    if (t >= 0.0 && Instructions_5pt5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instructions_5pt5.tStart = t;  // (not accounting for frame time here)
      Instructions_5pt5.frameNStart = frameN;  // exact frame index
      
      Instructions_5pt5.setAutoDraw(true);
    }
    
    
    // if Instructions_5pt5 is active this frame...
    if (Instructions_5pt5.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Instructions5pt5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instructions5pt5RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instructions5pt5' ---
    Instructions5pt5Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Instructions5pt5.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(NextPage_5.corr, level);
    }
    psychoJS.experiment.addData('NextPage_5.keys', NextPage_5.keys);
    if (typeof NextPage_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('NextPage_5.rt', NextPage_5.rt);
        psychoJS.experiment.addData('NextPage_5.duration', NextPage_5.duration);
        routineTimer.reset();
        }
    
    NextPage_5.stop();
    // the Routine "Instructions5pt5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Instructions6MaxDurationReached;
var _NextPage_6_allKeys;
var Instructions6MaxDuration;
var Instructions6Components;
function Instructions6RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instructions6' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    Instructions6Clock.reset();
    routineTimer.reset();
    Instructions6MaxDurationReached = false;
    // update component parameters for each repeat
    NextPage_6.keys = undefined;
    NextPage_6.rt = undefined;
    _NextPage_6_allKeys = [];
    psychoJS.experiment.addData('Instructions6.started', globalClock.getTime());
    Instructions6MaxDuration = null
    // keep track of which components have finished
    Instructions6Components = [];
    Instructions6Components.push(NextPage_6);
    Instructions6Components.push(Instructions_6);
    Instructions6Components.push(Instructions_6_Target);
    Instructions6Components.push(TargetImage);
    Instructions6Components.push(Instructions_6_Match);
    
    Instructions6Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Instructions6RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instructions6' ---
    // get current time
    t = Instructions6Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *NextPage_6* updates
    if (t >= 0.0 && NextPage_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      NextPage_6.tStart = t;  // (not accounting for frame time here)
      NextPage_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { NextPage_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { NextPage_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { NextPage_6.clearEvents(); });
    }
    
    // if NextPage_6 is active this frame...
    if (NextPage_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = NextPage_6.getKeys({
        keyList: typeof [matchKey] === 'string' ? [[matchKey]] : [matchKey], 
        waitRelease: false
      });
      _NextPage_6_allKeys = _NextPage_6_allKeys.concat(theseKeys);
      if (_NextPage_6_allKeys.length > 0) {
        NextPage_6.keys = _NextPage_6_allKeys[0].name;  // just the first key pressed
        NextPage_6.rt = _NextPage_6_allKeys[0].rt;
        NextPage_6.duration = _NextPage_6_allKeys[0].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Instructions_6* updates
    if (t >= 0.0 && Instructions_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instructions_6.tStart = t;  // (not accounting for frame time here)
      Instructions_6.frameNStart = frameN;  // exact frame index
      
      Instructions_6.setAutoDraw(true);
    }
    
    
    // if Instructions_6 is active this frame...
    if (Instructions_6.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *Instructions_6_Target* updates
    if (t >= 0.0 && Instructions_6_Target.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instructions_6_Target.tStart = t;  // (not accounting for frame time here)
      Instructions_6_Target.frameNStart = frameN;  // exact frame index
      
      Instructions_6_Target.setAutoDraw(true);
    }
    
    
    // if Instructions_6_Target is active this frame...
    if (Instructions_6_Target.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *TargetImage* updates
    if (t >= 0.0 && TargetImage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TargetImage.tStart = t;  // (not accounting for frame time here)
      TargetImage.frameNStart = frameN;  // exact frame index
      
      TargetImage.setAutoDraw(true);
    }
    
    
    // if TargetImage is active this frame...
    if (TargetImage.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *Instructions_6_Match* updates
    if (t >= 0.0 && Instructions_6_Match.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instructions_6_Match.tStart = t;  // (not accounting for frame time here)
      Instructions_6_Match.frameNStart = frameN;  // exact frame index
      
      Instructions_6_Match.setAutoDraw(true);
    }
    
    
    // if Instructions_6_Match is active this frame...
    if (Instructions_6_Match.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Instructions6Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instructions6RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instructions6' ---
    Instructions6Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Instructions6.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(NextPage_6.corr, level);
    }
    psychoJS.experiment.addData('NextPage_6.keys', NextPage_6.keys);
    if (typeof NextPage_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('NextPage_6.rt', NextPage_6.rt);
        psychoJS.experiment.addData('NextPage_6.duration', NextPage_6.duration);
        routineTimer.reset();
        }
    
    NextPage_6.stop();
    // the Routine "Instructions6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Instructions14MaxDurationReached;
var _NextPage_7_allKeys;
var Instructions14MaxDuration;
var Instructions14Components;
function Instructions14RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instructions14' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    Instructions14Clock.reset();
    routineTimer.reset();
    Instructions14MaxDurationReached = false;
    // update component parameters for each repeat
    NextPage_7.keys = undefined;
    NextPage_7.rt = undefined;
    _NextPage_7_allKeys = [];
    psychoJS.experiment.addData('Instructions14.started', globalClock.getTime());
    Instructions14MaxDuration = null
    // keep track of which components have finished
    Instructions14Components = [];
    Instructions14Components.push(NextPage_7);
    Instructions14Components.push(Instructions_14);
    
    Instructions14Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Instructions14RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instructions14' ---
    // get current time
    t = Instructions14Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *NextPage_7* updates
    if (t >= 0.0 && NextPage_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      NextPage_7.tStart = t;  // (not accounting for frame time here)
      NextPage_7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { NextPage_7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { NextPage_7.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { NextPage_7.clearEvents(); });
    }
    
    // if NextPage_7 is active this frame...
    if (NextPage_7.status === PsychoJS.Status.STARTED) {
      let theseKeys = NextPage_7.getKeys({
        keyList: typeof [noMatchKey] === 'string' ? [[noMatchKey]] : [noMatchKey], 
        waitRelease: false
      });
      _NextPage_7_allKeys = _NextPage_7_allKeys.concat(theseKeys);
      if (_NextPage_7_allKeys.length > 0) {
        NextPage_7.keys = _NextPage_7_allKeys[_NextPage_7_allKeys.length - 1].name;  // just the last key pressed
        NextPage_7.rt = _NextPage_7_allKeys[_NextPage_7_allKeys.length - 1].rt;
        NextPage_7.duration = _NextPage_7_allKeys[_NextPage_7_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Instructions_14* updates
    if (t >= 0.0 && Instructions_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instructions_14.tStart = t;  // (not accounting for frame time here)
      Instructions_14.frameNStart = frameN;  // exact frame index
      
      Instructions_14.setAutoDraw(true);
    }
    
    
    // if Instructions_14 is active this frame...
    if (Instructions_14.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Instructions14Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instructions14RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instructions14' ---
    Instructions14Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Instructions14.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(NextPage_7.corr, level);
    }
    psychoJS.experiment.addData('NextPage_7.keys', NextPage_7.keys);
    if (typeof NextPage_7.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('NextPage_7.rt', NextPage_7.rt);
        psychoJS.experiment.addData('NextPage_7.duration', NextPage_7.duration);
        routineTimer.reset();
        }
    
    NextPage_7.stop();
    // the Routine "Instructions14" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Instructions6pt2MaxDurationReached;
var _NextPage_8_allKeys;
var Instructions6pt2MaxDuration;
var Instructions6pt2Components;
function Instructions6pt2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instructions6pt2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    Instructions6pt2Clock.reset();
    routineTimer.reset();
    Instructions6pt2MaxDurationReached = false;
    // update component parameters for each repeat
    NextPage_8.keys = undefined;
    NextPage_8.rt = undefined;
    _NextPage_8_allKeys = [];
    psychoJS.experiment.addData('Instructions6pt2.started', globalClock.getTime());
    Instructions6pt2MaxDuration = null
    // keep track of which components have finished
    Instructions6pt2Components = [];
    Instructions6pt2Components.push(NextPage_8);
    Instructions6pt2Components.push(Instructions_6pt2);
    
    Instructions6pt2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Instructions6pt2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instructions6pt2' ---
    // get current time
    t = Instructions6pt2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *NextPage_8* updates
    if (t >= 0.0 && NextPage_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      NextPage_8.tStart = t;  // (not accounting for frame time here)
      NextPage_8.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { NextPage_8.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { NextPage_8.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { NextPage_8.clearEvents(); });
    }
    
    // if NextPage_8 is active this frame...
    if (NextPage_8.status === PsychoJS.Status.STARTED) {
      let theseKeys = NextPage_8.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _NextPage_8_allKeys = _NextPage_8_allKeys.concat(theseKeys);
      if (_NextPage_8_allKeys.length > 0) {
        NextPage_8.keys = _NextPage_8_allKeys[_NextPage_8_allKeys.length - 1].name;  // just the last key pressed
        NextPage_8.rt = _NextPage_8_allKeys[_NextPage_8_allKeys.length - 1].rt;
        NextPage_8.duration = _NextPage_8_allKeys[_NextPage_8_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Instructions_6pt2* updates
    if (t >= 0.0 && Instructions_6pt2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instructions_6pt2.tStart = t;  // (not accounting for frame time here)
      Instructions_6pt2.frameNStart = frameN;  // exact frame index
      
      Instructions_6pt2.setAutoDraw(true);
    }
    
    
    // if Instructions_6pt2 is active this frame...
    if (Instructions_6pt2.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Instructions6pt2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instructions6pt2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instructions6pt2' ---
    Instructions6pt2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Instructions6pt2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(NextPage_8.corr, level);
    }
    psychoJS.experiment.addData('NextPage_8.keys', NextPage_8.keys);
    if (typeof NextPage_8.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('NextPage_8.rt', NextPage_8.rt);
        psychoJS.experiment.addData('NextPage_8.duration', NextPage_8.duration);
        routineTimer.reset();
        }
    
    NextPage_8.stop();
    // the Routine "Instructions6pt2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var PracticeTrial1_CueMaxDurationReached;
var PracticeTrial1_CueMaxDuration;
var PracticeTrial1_CueComponents;
function PracticeTrial1_CueRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PracticeTrial1_Cue' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    PracticeTrial1_CueClock.reset(routineTimer.getTime());
    routineTimer.add(3.000000);
    PracticeTrial1_CueMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('PracticeTrial1_Cue.started', globalClock.getTime());
    PracticeTrial1_CueMaxDuration = null
    // keep track of which components have finished
    PracticeTrial1_CueComponents = [];
    PracticeTrial1_CueComponents.push(CueFix_1);
    PracticeTrial1_CueComponents.push(CueTarget_1);
    PracticeTrial1_CueComponents.push(CueTargetImage_1);
    
    PracticeTrial1_CueComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function PracticeTrial1_CueRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PracticeTrial1_Cue' ---
    // get current time
    t = PracticeTrial1_CueClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *CueFix_1* updates
    if (t >= 0.0 && CueFix_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CueFix_1.tStart = t;  // (not accounting for frame time here)
      CueFix_1.frameNStart = frameN;  // exact frame index
      
      CueFix_1.setAutoDraw(true);
    }
    
    
    // if CueFix_1 is active this frame...
    if (CueFix_1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (CueFix_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      CueFix_1.tStop = t;  // not accounting for scr refresh
      CueFix_1.frameNStop = frameN;  // exact frame index
      // update status
      CueFix_1.status = PsychoJS.Status.FINISHED;
      CueFix_1.setAutoDraw(false);
    }
    
    
    // *CueTarget_1* updates
    if (t >= 0.5 && CueTarget_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CueTarget_1.tStart = t;  // (not accounting for frame time here)
      CueTarget_1.frameNStart = frameN;  // exact frame index
      
      CueTarget_1.setAutoDraw(true);
    }
    
    
    // if CueTarget_1 is active this frame...
    if (CueTarget_1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (CueTarget_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      CueTarget_1.tStop = t;  // not accounting for scr refresh
      CueTarget_1.frameNStop = frameN;  // exact frame index
      // update status
      CueTarget_1.status = PsychoJS.Status.FINISHED;
      CueTarget_1.setAutoDraw(false);
    }
    
    
    // *CueTargetImage_1* updates
    if (t >= 0.5 && CueTargetImage_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CueTargetImage_1.tStart = t;  // (not accounting for frame time here)
      CueTargetImage_1.frameNStart = frameN;  // exact frame index
      
      CueTargetImage_1.setAutoDraw(true);
    }
    
    
    // if CueTargetImage_1 is active this frame...
    if (CueTargetImage_1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (CueTargetImage_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      CueTargetImage_1.tStop = t;  // not accounting for scr refresh
      CueTargetImage_1.frameNStop = frameN;  // exact frame index
      // update status
      CueTargetImage_1.status = PsychoJS.Status.FINISHED;
      CueTargetImage_1.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PracticeTrial1_CueComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PracticeTrial1_CueRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PracticeTrial1_Cue' ---
    PracticeTrial1_CueComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('PracticeTrial1_Cue.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (PracticeTrial1_CueMaxDurationReached) {
        PracticeTrial1_CueClock.add(PracticeTrial1_CueMaxDuration);
    } else {
        PracticeTrial1_CueClock.add(3.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practiceLoop;
function practiceLoopLoopBegin(practiceLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practiceLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'PracticeTrials1.xlsx',
      seed: undefined, name: 'practiceLoop'
    });
    psychoJS.experiment.addLoop(practiceLoop); // add the loop to the experiment
    currentLoop = practiceLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    practiceLoop.forEach(function() {
      snapshot = practiceLoop.getSnapshot();
    
      practiceLoopLoopScheduler.add(importConditions(snapshot));
      practiceLoopLoopScheduler.add(PracticeTrial_StimRoutineBegin(snapshot));
      practiceLoopLoopScheduler.add(PracticeTrial_StimRoutineEachFrame());
      practiceLoopLoopScheduler.add(PracticeTrial_StimRoutineEnd(snapshot));
      practiceLoopLoopScheduler.add(PracticeTrial_FeedbackRoutineBegin(snapshot));
      practiceLoopLoopScheduler.add(PracticeTrial_FeedbackRoutineEachFrame());
      practiceLoopLoopScheduler.add(PracticeTrial_FeedbackRoutineEnd(snapshot));
      practiceLoopLoopScheduler.add(practiceLoopLoopEndIteration(practiceLoopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function practiceLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practiceLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practiceLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var practiceLoop2;
function practiceLoop2LoopBegin(practiceLoop2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practiceLoop2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'PracticeTrials2.xlsx',
      seed: undefined, name: 'practiceLoop2'
    });
    psychoJS.experiment.addLoop(practiceLoop2); // add the loop to the experiment
    currentLoop = practiceLoop2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    practiceLoop2.forEach(function() {
      snapshot = practiceLoop2.getSnapshot();
    
      practiceLoop2LoopScheduler.add(importConditions(snapshot));
      practiceLoop2LoopScheduler.add(PracticeTrial_StimRoutineBegin(snapshot));
      practiceLoop2LoopScheduler.add(PracticeTrial_StimRoutineEachFrame());
      practiceLoop2LoopScheduler.add(PracticeTrial_StimRoutineEnd(snapshot));
      practiceLoop2LoopScheduler.add(PracticeTrial_FeedbackRoutineBegin(snapshot));
      practiceLoop2LoopScheduler.add(PracticeTrial_FeedbackRoutineEachFrame());
      practiceLoop2LoopScheduler.add(PracticeTrial_FeedbackRoutineEnd(snapshot));
      practiceLoop2LoopScheduler.add(practiceLoop2LoopEndIteration(practiceLoop2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function practiceLoop2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practiceLoop2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practiceLoop2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var practiceLoop3;
function practiceLoop3LoopBegin(practiceLoop3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practiceLoop3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'PracticeTrials3.xlsx',
      seed: undefined, name: 'practiceLoop3'
    });
    psychoJS.experiment.addLoop(practiceLoop3); // add the loop to the experiment
    currentLoop = practiceLoop3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    practiceLoop3.forEach(function() {
      snapshot = practiceLoop3.getSnapshot();
    
      practiceLoop3LoopScheduler.add(importConditions(snapshot));
      practiceLoop3LoopScheduler.add(PracticeTrial_StimRoutineBegin(snapshot));
      practiceLoop3LoopScheduler.add(PracticeTrial_StimRoutineEachFrame());
      practiceLoop3LoopScheduler.add(PracticeTrial_StimRoutineEnd(snapshot));
      practiceLoop3LoopScheduler.add(PracticeTrial_FeedbackRoutineBegin(snapshot));
      practiceLoop3LoopScheduler.add(PracticeTrial_FeedbackRoutineEachFrame());
      practiceLoop3LoopScheduler.add(PracticeTrial_FeedbackRoutineEnd(snapshot));
      practiceLoop3LoopScheduler.add(practiceLoop3LoopEndIteration(practiceLoop3LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function practiceLoop3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practiceLoop3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practiceLoop3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var practiceLoop4;
function practiceLoop4LoopBegin(practiceLoop4LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practiceLoop4 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'PracticeTrials4.xlsx',
      seed: undefined, name: 'practiceLoop4'
    });
    psychoJS.experiment.addLoop(practiceLoop4); // add the loop to the experiment
    currentLoop = practiceLoop4;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    practiceLoop4.forEach(function() {
      snapshot = practiceLoop4.getSnapshot();
    
      practiceLoop4LoopScheduler.add(importConditions(snapshot));
      practiceLoop4LoopScheduler.add(PracticeTrial_StimRoutineBegin(snapshot));
      practiceLoop4LoopScheduler.add(PracticeTrial_StimRoutineEachFrame());
      practiceLoop4LoopScheduler.add(PracticeTrial_StimRoutineEnd(snapshot));
      practiceLoop4LoopScheduler.add(PracticeTrial_FeedbackRoutineBegin(snapshot));
      practiceLoop4LoopScheduler.add(PracticeTrial_FeedbackRoutineEachFrame());
      practiceLoop4LoopScheduler.add(PracticeTrial_FeedbackRoutineEnd(snapshot));
      practiceLoop4LoopScheduler.add(practiceLoop4LoopEndIteration(practiceLoop4LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function practiceLoop4LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practiceLoop4);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practiceLoop4LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var practiceLoop5;
function practiceLoop5LoopBegin(practiceLoop5LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practiceLoop5 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'PracticeTrials5.xlsx',
      seed: undefined, name: 'practiceLoop5'
    });
    psychoJS.experiment.addLoop(practiceLoop5); // add the loop to the experiment
    currentLoop = practiceLoop5;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    practiceLoop5.forEach(function() {
      snapshot = practiceLoop5.getSnapshot();
    
      practiceLoop5LoopScheduler.add(importConditions(snapshot));
      practiceLoop5LoopScheduler.add(PracticeTrial_StimRoutineBegin(snapshot));
      practiceLoop5LoopScheduler.add(PracticeTrial_StimRoutineEachFrame());
      practiceLoop5LoopScheduler.add(PracticeTrial_StimRoutineEnd(snapshot));
      practiceLoop5LoopScheduler.add(PracticeTrial_FeedbackRoutineBegin(snapshot));
      practiceLoop5LoopScheduler.add(PracticeTrial_FeedbackRoutineEachFrame());
      practiceLoop5LoopScheduler.add(PracticeTrial_FeedbackRoutineEnd(snapshot));
      practiceLoop5LoopScheduler.add(practiceLoop5LoopEndIteration(practiceLoop5LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function practiceLoop5LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practiceLoop5);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practiceLoop5LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var practiceLoop6;
function practiceLoop6LoopBegin(practiceLoop6LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practiceLoop6 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'PracticeTrials6.xlsx',
      seed: undefined, name: 'practiceLoop6'
    });
    psychoJS.experiment.addLoop(practiceLoop6); // add the loop to the experiment
    currentLoop = practiceLoop6;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    practiceLoop6.forEach(function() {
      snapshot = practiceLoop6.getSnapshot();
    
      practiceLoop6LoopScheduler.add(importConditions(snapshot));
      practiceLoop6LoopScheduler.add(PracticeTrial_StimRoutineBegin(snapshot));
      practiceLoop6LoopScheduler.add(PracticeTrial_StimRoutineEachFrame());
      practiceLoop6LoopScheduler.add(PracticeTrial_StimRoutineEnd(snapshot));
      practiceLoop6LoopScheduler.add(PracticeTrial_FeedbackRoutineBegin(snapshot));
      practiceLoop6LoopScheduler.add(PracticeTrial_FeedbackRoutineEachFrame());
      practiceLoop6LoopScheduler.add(PracticeTrial_FeedbackRoutineEnd(snapshot));
      practiceLoop6LoopScheduler.add(practiceLoop6LoopEndIteration(practiceLoop6LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function practiceLoop6LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practiceLoop6);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practiceLoop6LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var practiceLoop7;
function practiceLoop7LoopBegin(practiceLoop7LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practiceLoop7 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'PracticeTrials7.xlsx',
      seed: undefined, name: 'practiceLoop7'
    });
    psychoJS.experiment.addLoop(practiceLoop7); // add the loop to the experiment
    currentLoop = practiceLoop7;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    practiceLoop7.forEach(function() {
      snapshot = practiceLoop7.getSnapshot();
    
      practiceLoop7LoopScheduler.add(importConditions(snapshot));
      practiceLoop7LoopScheduler.add(PracticeTrial_StimRoutineBegin(snapshot));
      practiceLoop7LoopScheduler.add(PracticeTrial_StimRoutineEachFrame());
      practiceLoop7LoopScheduler.add(PracticeTrial_StimRoutineEnd(snapshot));
      practiceLoop7LoopScheduler.add(PracticeTrial_FeedbackRoutineBegin(snapshot));
      practiceLoop7LoopScheduler.add(PracticeTrial_FeedbackRoutineEachFrame());
      practiceLoop7LoopScheduler.add(PracticeTrial_FeedbackRoutineEnd(snapshot));
      practiceLoop7LoopScheduler.add(practiceLoop7LoopEndIteration(practiceLoop7LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function practiceLoop7LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practiceLoop7);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practiceLoop7LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var practiceLoop8;
function practiceLoop8LoopBegin(practiceLoop8LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practiceLoop8 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'PracticeTrials8.xlsx',
      seed: undefined, name: 'practiceLoop8'
    });
    psychoJS.experiment.addLoop(practiceLoop8); // add the loop to the experiment
    currentLoop = practiceLoop8;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    practiceLoop8.forEach(function() {
      snapshot = practiceLoop8.getSnapshot();
    
      practiceLoop8LoopScheduler.add(importConditions(snapshot));
      practiceLoop8LoopScheduler.add(PracticeTrial_StimRoutineBegin(snapshot));
      practiceLoop8LoopScheduler.add(PracticeTrial_StimRoutineEachFrame());
      practiceLoop8LoopScheduler.add(PracticeTrial_StimRoutineEnd(snapshot));
      practiceLoop8LoopScheduler.add(PracticeTrial_FeedbackRoutineBegin(snapshot));
      practiceLoop8LoopScheduler.add(PracticeTrial_FeedbackRoutineEachFrame());
      practiceLoop8LoopScheduler.add(PracticeTrial_FeedbackRoutineEnd(snapshot));
      practiceLoop8LoopScheduler.add(practiceLoop8LoopEndIteration(practiceLoop8LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function practiceLoop8LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practiceLoop8);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practiceLoop8LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var PracticeTrial_StimMaxDurationReached;
var _response_allKeys;
var PracticeTrial_StimMaxDuration;
var PracticeTrial_StimComponents;
function PracticeTrial_StimRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PracticeTrial_Stim' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    PracticeTrial_StimClock.reset(routineTimer.getTime());
    routineTimer.add(2.000000);
    PracticeTrial_StimMaxDurationReached = false;
    // update component parameters for each repeat
    response.keys = undefined;
    response.rt = undefined;
    _response_allKeys = [];
    Stim.setImage(Stimulus);
    psychoJS.experiment.addData('PracticeTrial_Stim.started', globalClock.getTime());
    PracticeTrial_StimMaxDuration = null
    // keep track of which components have finished
    PracticeTrial_StimComponents = [];
    PracticeTrial_StimComponents.push(response);
    PracticeTrial_StimComponents.push(Stim);
    PracticeTrial_StimComponents.push(Stim_Match);
    PracticeTrial_StimComponents.push(Stim_No_Match);
    
    PracticeTrial_StimComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PracticeTrial_StimRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PracticeTrial_Stim' ---
    // get current time
    t = PracticeTrial_StimClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *response* updates
    if (t >= 0.0 && response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response.tStart = t;  // (not accounting for frame time here)
      response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { response.clearEvents(); });
    }
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (response.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      response.tStop = t;  // not accounting for scr refresh
      response.frameNStop = frameN;  // exact frame index
      // update status
      response.status = PsychoJS.Status.FINISHED;
      frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (response.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        response.tStop = t;  // not accounting for scr refresh
        response.frameNStop = frameN;  // exact frame index
        // update status
        response.status = PsychoJS.Status.FINISHED;
        response.status = PsychoJS.Status.FINISHED;
          }
        
      }
      
      // if response is active this frame...
      if (response.status === PsychoJS.Status.STARTED) {
        let theseKeys = response.getKeys({
          keyList: typeof [[matchKey,noMatchKey]] === 'string' ? [[[matchKey,noMatchKey]]] : [[matchKey,noMatchKey]], 
          waitRelease: false
        });
        _response_allKeys = _response_allKeys.concat(theseKeys);
        if (_response_allKeys.length > 0) {
          response.keys = _response_allKeys[0].name;  // just the first key pressed
          response.rt = _response_allKeys[0].rt;
          response.duration = _response_allKeys[0].duration;
          // was this correct?
          if (response.keys == correctKey) {
              response.corr = 1;
          } else {
              response.corr = 0;
          }
        }
      }
      
      
      // *Stim* updates
      if (t >= 0 && Stim.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Stim.tStart = t;  // (not accounting for frame time here)
        Stim.frameNStart = frameN;  // exact frame index
        
        Stim.setAutoDraw(true);
      }
      
      
      // if Stim is active this frame...
      if (Stim.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (Stim.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        Stim.tStop = t;  // not accounting for scr refresh
        Stim.frameNStop = frameN;  // exact frame index
        // update status
        Stim.status = PsychoJS.Status.FINISHED;
        Stim.setAutoDraw(false);
      }
      
      
      // *Stim_Match* updates
      if (t >= 0 && Stim_Match.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Stim_Match.tStart = t;  // (not accounting for frame time here)
        Stim_Match.frameNStart = frameN;  // exact frame index
        
        Stim_Match.setAutoDraw(true);
      }
      
      
      // if Stim_Match is active this frame...
      if (Stim_Match.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (Stim_Match.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        Stim_Match.tStop = t;  // not accounting for scr refresh
        Stim_Match.frameNStop = frameN;  // exact frame index
        // update status
        Stim_Match.status = PsychoJS.Status.FINISHED;
        Stim_Match.setAutoDraw(false);
      }
      
      
      // *Stim_No_Match* updates
      if (t >= 0 && Stim_No_Match.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Stim_No_Match.tStart = t;  // (not accounting for frame time here)
        Stim_No_Match.frameNStart = frameN;  // exact frame index
        
        Stim_No_Match.setAutoDraw(true);
      }
      
      
      // if Stim_No_Match is active this frame...
      if (Stim_No_Match.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (Stim_No_Match.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        Stim_No_Match.tStop = t;  // not accounting for scr refresh
        Stim_No_Match.frameNStop = frameN;  // exact frame index
        // update status
        Stim_No_Match.status = PsychoJS.Status.FINISHED;
        Stim_No_Match.setAutoDraw(false);
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      PracticeTrial_StimComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
var fbText;
var fbColor;
function PracticeTrial_StimRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'PracticeTrial_Stim' ---
      PracticeTrial_StimComponents.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('PracticeTrial_Stim.stopped', globalClock.getTime());
      // was no response the correct answer?!
      if (response.keys === undefined) {
        if (['None','none',undefined].includes(correctKey)) {
           response.corr = 1;  // correct non-response
        } else {
           response.corr = 0;  // failed to respond (incorrectly)
        }
      }
      // store data for current loop
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(response.corr, level);
      }
      psychoJS.experiment.addData('response.keys', response.keys);
      psychoJS.experiment.addData('response.corr', response.corr);
      if (typeof response.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('response.rt', response.rt);
          psychoJS.experiment.addData('response.duration', response.duration);
          }
      
      response.stop();
      // Run 'End Routine' code from feedbackLogic
      if ((response.keys === null)) {
          fbText = "No response detected.";
          fbColor = "yellow";
      } else {
          if (response.corr) {
              fbText = "Correct!";
              fbColor = "limegreen";
          } else {
              fbText = "Incorrect";
              fbColor = "red";
          }
      }
      psychoJS.experiment.addData("DEBUG_TargetType", TargetType);
      psychoJS.experiment.addData("DEBUG_correctKey", correctKey);
      
      if (routineForceEnded) {
          routineTimer.reset();} else if (PracticeTrial_StimMaxDurationReached) {
          PracticeTrial_StimClock.add(PracticeTrial_StimMaxDuration);
      } else {
          PracticeTrial_StimClock.add(2.000000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var PracticeTrial_FeedbackMaxDurationReached;
var PracticeTrial_FeedbackMaxDuration;
var PracticeTrial_FeedbackComponents;
function PracticeTrial_FeedbackRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'PracticeTrial_Feedback' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      PracticeTrial_FeedbackClock.reset(routineTimer.getTime());
      routineTimer.add(2.000000);
      PracticeTrial_FeedbackMaxDurationReached = false;
      // update component parameters for each repeat
      Feedback.setColor(new util.Color(fbColor));
      Feedback.setText(fbText);
      psychoJS.experiment.addData('PracticeTrial_Feedback.started', globalClock.getTime());
      PracticeTrial_FeedbackMaxDuration = null
      // keep track of which components have finished
      PracticeTrial_FeedbackComponents = [];
      PracticeTrial_FeedbackComponents.push(Fix);
      PracticeTrial_FeedbackComponents.push(Feedback);
      
      PracticeTrial_FeedbackComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function PracticeTrial_FeedbackRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'PracticeTrial_Feedback' ---
      // get current time
      t = PracticeTrial_FeedbackClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *Fix* updates
      if (t >= 0 && Fix.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Fix.tStart = t;  // (not accounting for frame time here)
        Fix.frameNStart = frameN;  // exact frame index
        
        Fix.setAutoDraw(true);
      }
      
      
      // if Fix is active this frame...
      if (Fix.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (Fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        Fix.tStop = t;  // not accounting for scr refresh
        Fix.frameNStop = frameN;  // exact frame index
        // update status
        Fix.status = PsychoJS.Status.FINISHED;
        Fix.setAutoDraw(false);
      }
      
      
      // *Feedback* updates
      if (t >= 0.5 && Feedback.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Feedback.tStart = t;  // (not accounting for frame time here)
        Feedback.frameNStart = frameN;  // exact frame index
        
        Feedback.setAutoDraw(true);
      }
      
      
      // if Feedback is active this frame...
      if (Feedback.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.5 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (Feedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        Feedback.tStop = t;  // not accounting for scr refresh
        Feedback.frameNStop = frameN;  // exact frame index
        // update status
        Feedback.status = PsychoJS.Status.FINISHED;
        Feedback.setAutoDraw(false);
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      PracticeTrial_FeedbackComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function PracticeTrial_FeedbackRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'PracticeTrial_Feedback' ---
      PracticeTrial_FeedbackComponents.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('PracticeTrial_Feedback.stopped', globalClock.getTime());
      if (routineForceEnded) {
          routineTimer.reset();} else if (PracticeTrial_FeedbackMaxDurationReached) {
          PracticeTrial_FeedbackClock.add(PracticeTrial_FeedbackMaxDuration);
      } else {
          PracticeTrial_FeedbackClock.add(2.000000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var InstructionsSpaceToContinueMaxDurationReached;
var _NextPage_9_allKeys;
var InstructionsSpaceToContinueMaxDuration;
var InstructionsSpaceToContinueComponents;
function InstructionsSpaceToContinueRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'InstructionsSpaceToContinue' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      InstructionsSpaceToContinueClock.reset();
      routineTimer.reset();
      InstructionsSpaceToContinueMaxDurationReached = false;
      // update component parameters for each repeat
      NextPage_9.keys = undefined;
      NextPage_9.rt = undefined;
      _NextPage_9_allKeys = [];
      psychoJS.experiment.addData('InstructionsSpaceToContinue.started', globalClock.getTime());
      InstructionsSpaceToContinueMaxDuration = null
      // keep track of which components have finished
      InstructionsSpaceToContinueComponents = [];
      InstructionsSpaceToContinueComponents.push(NextPage_9);
      InstructionsSpaceToContinueComponents.push(Instructions_Space);
      
      InstructionsSpaceToContinueComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function InstructionsSpaceToContinueRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'InstructionsSpaceToContinue' ---
      // get current time
      t = InstructionsSpaceToContinueClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *NextPage_9* updates
      if (t >= 0.0 && NextPage_9.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        NextPage_9.tStart = t;  // (not accounting for frame time here)
        NextPage_9.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { NextPage_9.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { NextPage_9.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { NextPage_9.clearEvents(); });
      }
      
      // if NextPage_9 is active this frame...
      if (NextPage_9.status === PsychoJS.Status.STARTED) {
        let theseKeys = NextPage_9.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _NextPage_9_allKeys = _NextPage_9_allKeys.concat(theseKeys);
        if (_NextPage_9_allKeys.length > 0) {
          NextPage_9.keys = _NextPage_9_allKeys[_NextPage_9_allKeys.length - 1].name;  // just the last key pressed
          NextPage_9.rt = _NextPage_9_allKeys[_NextPage_9_allKeys.length - 1].rt;
          NextPage_9.duration = _NextPage_9_allKeys[_NextPage_9_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      
      // *Instructions_Space* updates
      if (t >= 0.0 && Instructions_Space.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Instructions_Space.tStart = t;  // (not accounting for frame time here)
        Instructions_Space.frameNStart = frameN;  // exact frame index
        
        Instructions_Space.setAutoDraw(true);
      }
      
      
      // if Instructions_Space is active this frame...
      if (Instructions_Space.status === PsychoJS.Status.STARTED) {
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      InstructionsSpaceToContinueComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function InstructionsSpaceToContinueRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'InstructionsSpaceToContinue' ---
      InstructionsSpaceToContinueComponents.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('InstructionsSpaceToContinue.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(NextPage_9.corr, level);
      }
      psychoJS.experiment.addData('NextPage_9.keys', NextPage_9.keys);
      if (typeof NextPage_9.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('NextPage_9.rt', NextPage_9.rt);
          psychoJS.experiment.addData('NextPage_9.duration', NextPage_9.duration);
          routineTimer.reset();
          }
      
      NextPage_9.stop();
      // the Routine "InstructionsSpaceToContinue" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var PracticeTrial2_CueMaxDurationReached;
var PracticeTrial2_CueMaxDuration;
var PracticeTrial2_CueComponents;
function PracticeTrial2_CueRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'PracticeTrial2_Cue' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      PracticeTrial2_CueClock.reset(routineTimer.getTime());
      routineTimer.add(3.000000);
      PracticeTrial2_CueMaxDurationReached = false;
      // update component parameters for each repeat
      psychoJS.experiment.addData('PracticeTrial2_Cue.started', globalClock.getTime());
      PracticeTrial2_CueMaxDuration = null
      // keep track of which components have finished
      PracticeTrial2_CueComponents = [];
      PracticeTrial2_CueComponents.push(CueFix_2);
      PracticeTrial2_CueComponents.push(CueTarget_2);
      PracticeTrial2_CueComponents.push(CueTargetImage_2);
      
      PracticeTrial2_CueComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function PracticeTrial2_CueRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'PracticeTrial2_Cue' ---
      // get current time
      t = PracticeTrial2_CueClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *CueFix_2* updates
      if (t >= 0.0 && CueFix_2.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        CueFix_2.tStart = t;  // (not accounting for frame time here)
        CueFix_2.frameNStart = frameN;  // exact frame index
        
        CueFix_2.setAutoDraw(true);
      }
      
      
      // if CueFix_2 is active this frame...
      if (CueFix_2.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (CueFix_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        CueFix_2.tStop = t;  // not accounting for scr refresh
        CueFix_2.frameNStop = frameN;  // exact frame index
        // update status
        CueFix_2.status = PsychoJS.Status.FINISHED;
        CueFix_2.setAutoDraw(false);
      }
      
      
      // *CueTarget_2* updates
      if (t >= 0.5 && CueTarget_2.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        CueTarget_2.tStart = t;  // (not accounting for frame time here)
        CueTarget_2.frameNStart = frameN;  // exact frame index
        
        CueTarget_2.setAutoDraw(true);
      }
      
      
      // if CueTarget_2 is active this frame...
      if (CueTarget_2.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.5 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (CueTarget_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        CueTarget_2.tStop = t;  // not accounting for scr refresh
        CueTarget_2.frameNStop = frameN;  // exact frame index
        // update status
        CueTarget_2.status = PsychoJS.Status.FINISHED;
        CueTarget_2.setAutoDraw(false);
      }
      
      
      // *CueTargetImage_2* updates
      if (t >= 0.5 && CueTargetImage_2.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        CueTargetImage_2.tStart = t;  // (not accounting for frame time here)
        CueTargetImage_2.frameNStart = frameN;  // exact frame index
        
        CueTargetImage_2.setAutoDraw(true);
      }
      
      
      // if CueTargetImage_2 is active this frame...
      if (CueTargetImage_2.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.5 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (CueTargetImage_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        CueTargetImage_2.tStop = t;  // not accounting for scr refresh
        CueTargetImage_2.frameNStop = frameN;  // exact frame index
        // update status
        CueTargetImage_2.status = PsychoJS.Status.FINISHED;
        CueTargetImage_2.setAutoDraw(false);
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      PracticeTrial2_CueComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function PracticeTrial2_CueRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'PracticeTrial2_Cue' ---
      PracticeTrial2_CueComponents.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('PracticeTrial2_Cue.stopped', globalClock.getTime());
      if (routineForceEnded) {
          routineTimer.reset();} else if (PracticeTrial2_CueMaxDurationReached) {
          PracticeTrial2_CueClock.add(PracticeTrial2_CueMaxDuration);
      } else {
          PracticeTrial2_CueClock.add(3.000000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var Instructions8MaxDurationReached;
var _NextPage_10_allKeys;
var Instructions8MaxDuration;
var Instructions8Components;
function Instructions8RoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'Instructions8' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      Instructions8Clock.reset();
      routineTimer.reset();
      Instructions8MaxDurationReached = false;
      // update component parameters for each repeat
      NextPage_10.keys = undefined;
      NextPage_10.rt = undefined;
      _NextPage_10_allKeys = [];
      psychoJS.experiment.addData('Instructions8.started', globalClock.getTime());
      Instructions8MaxDuration = null
      // keep track of which components have finished
      Instructions8Components = [];
      Instructions8Components.push(NextPage_10);
      Instructions8Components.push(Instructions_8);
      
      Instructions8Components.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function Instructions8RoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'Instructions8' ---
      // get current time
      t = Instructions8Clock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *NextPage_10* updates
      if (t >= 0.0 && NextPage_10.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        NextPage_10.tStart = t;  // (not accounting for frame time here)
        NextPage_10.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { NextPage_10.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { NextPage_10.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { NextPage_10.clearEvents(); });
      }
      
      // if NextPage_10 is active this frame...
      if (NextPage_10.status === PsychoJS.Status.STARTED) {
        let theseKeys = NextPage_10.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _NextPage_10_allKeys = _NextPage_10_allKeys.concat(theseKeys);
        if (_NextPage_10_allKeys.length > 0) {
          NextPage_10.keys = _NextPage_10_allKeys[_NextPage_10_allKeys.length - 1].name;  // just the last key pressed
          NextPage_10.rt = _NextPage_10_allKeys[_NextPage_10_allKeys.length - 1].rt;
          NextPage_10.duration = _NextPage_10_allKeys[_NextPage_10_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      
      // *Instructions_8* updates
      if (t >= 0.0 && Instructions_8.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Instructions_8.tStart = t;  // (not accounting for frame time here)
        Instructions_8.frameNStart = frameN;  // exact frame index
        
        Instructions_8.setAutoDraw(true);
      }
      
      
      // if Instructions_8 is active this frame...
      if (Instructions_8.status === PsychoJS.Status.STARTED) {
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      Instructions8Components.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function Instructions8RoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'Instructions8' ---
      Instructions8Components.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('Instructions8.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(NextPage_10.corr, level);
      }
      psychoJS.experiment.addData('NextPage_10.keys', NextPage_10.keys);
      if (typeof NextPage_10.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('NextPage_10.rt', NextPage_10.rt);
          psychoJS.experiment.addData('NextPage_10.duration', NextPage_10.duration);
          routineTimer.reset();
          }
      
      NextPage_10.stop();
      // the Routine "Instructions8" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var Instructions11MaxDurationReached;
var _NextPage_11_allKeys;
var Instructions11MaxDuration;
var Instructions11Components;
function Instructions11RoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'Instructions11' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      Instructions11Clock.reset();
      routineTimer.reset();
      Instructions11MaxDurationReached = false;
      // update component parameters for each repeat
      NextPage_11.keys = undefined;
      NextPage_11.rt = undefined;
      _NextPage_11_allKeys = [];
      psychoJS.experiment.addData('Instructions11.started', globalClock.getTime());
      Instructions11MaxDuration = null
      // keep track of which components have finished
      Instructions11Components = [];
      Instructions11Components.push(NextPage_11);
      Instructions11Components.push(Instructions_11);
      
      Instructions11Components.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function Instructions11RoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'Instructions11' ---
      // get current time
      t = Instructions11Clock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *NextPage_11* updates
      if (t >= 0.0 && NextPage_11.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        NextPage_11.tStart = t;  // (not accounting for frame time here)
        NextPage_11.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { NextPage_11.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { NextPage_11.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { NextPage_11.clearEvents(); });
      }
      
      // if NextPage_11 is active this frame...
      if (NextPage_11.status === PsychoJS.Status.STARTED) {
        let theseKeys = NextPage_11.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _NextPage_11_allKeys = _NextPage_11_allKeys.concat(theseKeys);
        if (_NextPage_11_allKeys.length > 0) {
          NextPage_11.keys = _NextPage_11_allKeys[_NextPage_11_allKeys.length - 1].name;  // just the last key pressed
          NextPage_11.rt = _NextPage_11_allKeys[_NextPage_11_allKeys.length - 1].rt;
          NextPage_11.duration = _NextPage_11_allKeys[_NextPage_11_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      
      // *Instructions_11* updates
      if (t >= 0.0 && Instructions_11.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Instructions_11.tStart = t;  // (not accounting for frame time here)
        Instructions_11.frameNStart = frameN;  // exact frame index
        
        Instructions_11.setAutoDraw(true);
      }
      
      
      // if Instructions_11 is active this frame...
      if (Instructions_11.status === PsychoJS.Status.STARTED) {
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      Instructions11Components.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function Instructions11RoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'Instructions11' ---
      Instructions11Components.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('Instructions11.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(NextPage_11.corr, level);
      }
      psychoJS.experiment.addData('NextPage_11.keys', NextPage_11.keys);
      if (typeof NextPage_11.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('NextPage_11.rt', NextPage_11.rt);
          psychoJS.experiment.addData('NextPage_11.duration', NextPage_11.duration);
          routineTimer.reset();
          }
      
      NextPage_11.stop();
      // the Routine "Instructions11" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var Instructions9MaxDurationReached;
var _NextPage_12_allKeys;
var Instructions9MaxDuration;
var Instructions9Components;
function Instructions9RoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'Instructions9' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      Instructions9Clock.reset();
      routineTimer.reset();
      Instructions9MaxDurationReached = false;
      // update component parameters for each repeat
      NextPage_12.keys = undefined;
      NextPage_12.rt = undefined;
      _NextPage_12_allKeys = [];
      Example_Stim.setImage('VM Stimuli/PracticeFO1.bmp');
      psychoJS.experiment.addData('Instructions9.started', globalClock.getTime());
      Instructions9MaxDuration = null
      // keep track of which components have finished
      Instructions9Components = [];
      Instructions9Components.push(NextPage_12);
      Instructions9Components.push(Instructions_9);
      Instructions9Components.push(Example_Stim);
      Instructions9Components.push(Example_Match);
      Instructions9Components.push(Example_No_Match);
      
      Instructions9Components.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function Instructions9RoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'Instructions9' ---
      // get current time
      t = Instructions9Clock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *NextPage_12* updates
      if (t >= 0.0 && NextPage_12.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        NextPage_12.tStart = t;  // (not accounting for frame time here)
        NextPage_12.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { NextPage_12.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { NextPage_12.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { NextPage_12.clearEvents(); });
      }
      
      // if NextPage_12 is active this frame...
      if (NextPage_12.status === PsychoJS.Status.STARTED) {
        let theseKeys = NextPage_12.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _NextPage_12_allKeys = _NextPage_12_allKeys.concat(theseKeys);
        if (_NextPage_12_allKeys.length > 0) {
          NextPage_12.keys = _NextPage_12_allKeys[_NextPage_12_allKeys.length - 1].name;  // just the last key pressed
          NextPage_12.rt = _NextPage_12_allKeys[_NextPage_12_allKeys.length - 1].rt;
          NextPage_12.duration = _NextPage_12_allKeys[_NextPage_12_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      
      // *Instructions_9* updates
      if (t >= 0.0 && Instructions_9.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Instructions_9.tStart = t;  // (not accounting for frame time here)
        Instructions_9.frameNStart = frameN;  // exact frame index
        
        Instructions_9.setAutoDraw(true);
      }
      
      
      // if Instructions_9 is active this frame...
      if (Instructions_9.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim* updates
      if (t >= 0 && Example_Stim.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim.tStart = t;  // (not accounting for frame time here)
        Example_Stim.frameNStart = frameN;  // exact frame index
        
        Example_Stim.setAutoDraw(true);
      }
      
      
      // if Example_Stim is active this frame...
      if (Example_Stim.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Match* updates
      if (t >= 0 && Example_Match.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Match.tStart = t;  // (not accounting for frame time here)
        Example_Match.frameNStart = frameN;  // exact frame index
        
        Example_Match.setAutoDraw(true);
      }
      
      
      // if Example_Match is active this frame...
      if (Example_Match.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_No_Match* updates
      if (t >= 0 && Example_No_Match.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_No_Match.tStart = t;  // (not accounting for frame time here)
        Example_No_Match.frameNStart = frameN;  // exact frame index
        
        Example_No_Match.setAutoDraw(true);
      }
      
      
      // if Example_No_Match is active this frame...
      if (Example_No_Match.status === PsychoJS.Status.STARTED) {
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      Instructions9Components.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function Instructions9RoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'Instructions9' ---
      Instructions9Components.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('Instructions9.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(NextPage_12.corr, level);
      }
      psychoJS.experiment.addData('NextPage_12.keys', NextPage_12.keys);
      if (typeof NextPage_12.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('NextPage_12.rt', NextPage_12.rt);
          psychoJS.experiment.addData('NextPage_12.duration', NextPage_12.duration);
          routineTimer.reset();
          }
      
      NextPage_12.stop();
      // the Routine "Instructions9" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var Instructions21MaxDurationReached;
var _NextPage_13_allKeys;
var Instructions21MaxDuration;
var Instructions21Components;
function Instructions21RoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'Instructions21' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      Instructions21Clock.reset();
      routineTimer.reset();
      Instructions21MaxDurationReached = false;
      // update component parameters for each repeat
      NextPage_13.keys = undefined;
      NextPage_13.rt = undefined;
      _NextPage_13_allKeys = [];
      Example_Stim_2.setImage('VM Stimuli/PracticeFO2.bmp');
      psychoJS.experiment.addData('Instructions21.started', globalClock.getTime());
      Instructions21MaxDuration = null
      // keep track of which components have finished
      Instructions21Components = [];
      Instructions21Components.push(NextPage_13);
      Instructions21Components.push(Instructions_21);
      Instructions21Components.push(One_Back_Example_Stim);
      Instructions21Components.push(Example_Stim_2);
      Instructions21Components.push(Example_Match_2);
      Instructions21Components.push(Example_No_Match_2);
      
      Instructions21Components.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function Instructions21RoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'Instructions21' ---
      // get current time
      t = Instructions21Clock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *NextPage_13* updates
      if (t >= 0.0 && NextPage_13.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        NextPage_13.tStart = t;  // (not accounting for frame time here)
        NextPage_13.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { NextPage_13.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { NextPage_13.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { NextPage_13.clearEvents(); });
      }
      
      // if NextPage_13 is active this frame...
      if (NextPage_13.status === PsychoJS.Status.STARTED) {
        let theseKeys = NextPage_13.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _NextPage_13_allKeys = _NextPage_13_allKeys.concat(theseKeys);
        if (_NextPage_13_allKeys.length > 0) {
          NextPage_13.keys = _NextPage_13_allKeys[_NextPage_13_allKeys.length - 1].name;  // just the last key pressed
          NextPage_13.rt = _NextPage_13_allKeys[_NextPage_13_allKeys.length - 1].rt;
          NextPage_13.duration = _NextPage_13_allKeys[_NextPage_13_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      
      // *Instructions_21* updates
      if (t >= 0.0 && Instructions_21.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Instructions_21.tStart = t;  // (not accounting for frame time here)
        Instructions_21.frameNStart = frameN;  // exact frame index
        
        Instructions_21.setAutoDraw(true);
      }
      
      
      // if Instructions_21 is active this frame...
      if (Instructions_21.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *One_Back_Example_Stim* updates
      if (t >= 0.0 && One_Back_Example_Stim.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        One_Back_Example_Stim.tStart = t;  // (not accounting for frame time here)
        One_Back_Example_Stim.frameNStart = frameN;  // exact frame index
        
        One_Back_Example_Stim.setAutoDraw(true);
      }
      
      
      // if One_Back_Example_Stim is active this frame...
      if (One_Back_Example_Stim.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_2* updates
      if (t >= 0 && Example_Stim_2.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_2.tStart = t;  // (not accounting for frame time here)
        Example_Stim_2.frameNStart = frameN;  // exact frame index
        
        Example_Stim_2.setAutoDraw(true);
      }
      
      
      // if Example_Stim_2 is active this frame...
      if (Example_Stim_2.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Match_2* updates
      if (t >= 0 && Example_Match_2.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Match_2.tStart = t;  // (not accounting for frame time here)
        Example_Match_2.frameNStart = frameN;  // exact frame index
        
        Example_Match_2.setAutoDraw(true);
      }
      
      
      // if Example_Match_2 is active this frame...
      if (Example_Match_2.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_No_Match_2* updates
      if (t >= 0 && Example_No_Match_2.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_No_Match_2.tStart = t;  // (not accounting for frame time here)
        Example_No_Match_2.frameNStart = frameN;  // exact frame index
        
        Example_No_Match_2.setAutoDraw(true);
      }
      
      
      // if Example_No_Match_2 is active this frame...
      if (Example_No_Match_2.status === PsychoJS.Status.STARTED) {
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      Instructions21Components.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function Instructions21RoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'Instructions21' ---
      Instructions21Components.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('Instructions21.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(NextPage_13.corr, level);
      }
      psychoJS.experiment.addData('NextPage_13.keys', NextPage_13.keys);
      if (typeof NextPage_13.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('NextPage_13.rt', NextPage_13.rt);
          psychoJS.experiment.addData('NextPage_13.duration', NextPage_13.duration);
          routineTimer.reset();
          }
      
      NextPage_13.stop();
      // the Routine "Instructions21" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var Instructions24MaxDurationReached;
var _NextPage_14_allKeys;
var Instructions24MaxDuration;
var Instructions24Components;
function Instructions24RoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'Instructions24' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      Instructions24Clock.reset();
      routineTimer.reset();
      Instructions24MaxDurationReached = false;
      // update component parameters for each repeat
      NextPage_14.keys = undefined;
      NextPage_14.rt = undefined;
      _NextPage_14_allKeys = [];
      Example_Stim_3.setImage('VM Stimuli/PracticeFO1.bmp');
      psychoJS.experiment.addData('Instructions24.started', globalClock.getTime());
      Instructions24MaxDuration = null
      // keep track of which components have finished
      Instructions24Components = [];
      Instructions24Components.push(NextPage_14);
      Instructions24Components.push(Instructions_24);
      Instructions24Components.push(Green_Border);
      Instructions24Components.push(Two_Back_Example_Stim);
      Instructions24Components.push(One_Back_Example_Stim_2);
      Instructions24Components.push(Example_Stim_3);
      Instructions24Components.push(Example_Match_3);
      Instructions24Components.push(Example_No_Match_3);
      
      Instructions24Components.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function Instructions24RoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'Instructions24' ---
      // get current time
      t = Instructions24Clock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *NextPage_14* updates
      if (t >= 0.0 && NextPage_14.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        NextPage_14.tStart = t;  // (not accounting for frame time here)
        NextPage_14.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { NextPage_14.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { NextPage_14.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { NextPage_14.clearEvents(); });
      }
      
      // if NextPage_14 is active this frame...
      if (NextPage_14.status === PsychoJS.Status.STARTED) {
        let theseKeys = NextPage_14.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _NextPage_14_allKeys = _NextPage_14_allKeys.concat(theseKeys);
        if (_NextPage_14_allKeys.length > 0) {
          NextPage_14.keys = _NextPage_14_allKeys[_NextPage_14_allKeys.length - 1].name;  // just the last key pressed
          NextPage_14.rt = _NextPage_14_allKeys[_NextPage_14_allKeys.length - 1].rt;
          NextPage_14.duration = _NextPage_14_allKeys[_NextPage_14_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      
      // *Instructions_24* updates
      if (t >= 0.0 && Instructions_24.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Instructions_24.tStart = t;  // (not accounting for frame time here)
        Instructions_24.frameNStart = frameN;  // exact frame index
        
        Instructions_24.setAutoDraw(true);
      }
      
      
      // if Instructions_24 is active this frame...
      if (Instructions_24.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Green_Border* updates
      if (t >= 0.0 && Green_Border.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Green_Border.tStart = t;  // (not accounting for frame time here)
        Green_Border.frameNStart = frameN;  // exact frame index
        
        Green_Border.setAutoDraw(true);
      }
      
      
      // if Green_Border is active this frame...
      if (Green_Border.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Two_Back_Example_Stim* updates
      if (t >= 0.0 && Two_Back_Example_Stim.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Two_Back_Example_Stim.tStart = t;  // (not accounting for frame time here)
        Two_Back_Example_Stim.frameNStart = frameN;  // exact frame index
        
        Two_Back_Example_Stim.setAutoDraw(true);
      }
      
      
      // if Two_Back_Example_Stim is active this frame...
      if (Two_Back_Example_Stim.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *One_Back_Example_Stim_2* updates
      if (t >= 0.0 && One_Back_Example_Stim_2.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        One_Back_Example_Stim_2.tStart = t;  // (not accounting for frame time here)
        One_Back_Example_Stim_2.frameNStart = frameN;  // exact frame index
        
        One_Back_Example_Stim_2.setAutoDraw(true);
      }
      
      
      // if One_Back_Example_Stim_2 is active this frame...
      if (One_Back_Example_Stim_2.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_3* updates
      if (t >= 0 && Example_Stim_3.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_3.tStart = t;  // (not accounting for frame time here)
        Example_Stim_3.frameNStart = frameN;  // exact frame index
        
        Example_Stim_3.setAutoDraw(true);
      }
      
      
      // if Example_Stim_3 is active this frame...
      if (Example_Stim_3.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Match_3* updates
      if (t >= 0 && Example_Match_3.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Match_3.tStart = t;  // (not accounting for frame time here)
        Example_Match_3.frameNStart = frameN;  // exact frame index
        
        Example_Match_3.setAutoDraw(true);
      }
      
      
      // if Example_Match_3 is active this frame...
      if (Example_Match_3.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_No_Match_3* updates
      if (t >= 0 && Example_No_Match_3.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_No_Match_3.tStart = t;  // (not accounting for frame time here)
        Example_No_Match_3.frameNStart = frameN;  // exact frame index
        
        Example_No_Match_3.setAutoDraw(true);
      }
      
      
      // if Example_No_Match_3 is active this frame...
      if (Example_No_Match_3.status === PsychoJS.Status.STARTED) {
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      Instructions24Components.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function Instructions24RoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'Instructions24' ---
      Instructions24Components.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('Instructions24.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(NextPage_14.corr, level);
      }
      psychoJS.experiment.addData('NextPage_14.keys', NextPage_14.keys);
      if (typeof NextPage_14.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('NextPage_14.rt', NextPage_14.rt);
          psychoJS.experiment.addData('NextPage_14.duration', NextPage_14.duration);
          routineTimer.reset();
          }
      
      NextPage_14.stop();
      // the Routine "Instructions24" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var Instructions25MaxDurationReached;
var _NextPage_15_allKeys;
var Instructions25MaxDuration;
var Instructions25Components;
function Instructions25RoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'Instructions25' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      Instructions25Clock.reset();
      routineTimer.reset();
      Instructions25MaxDurationReached = false;
      // update component parameters for each repeat
      NextPage_15.keys = undefined;
      NextPage_15.rt = undefined;
      _NextPage_15_allKeys = [];
      Example_Stim_4.setImage('VM Stimuli/PracticeFO3.bmp');
      psychoJS.experiment.addData('Instructions25.started', globalClock.getTime());
      Instructions25MaxDuration = null
      // keep track of which components have finished
      Instructions25Components = [];
      Instructions25Components.push(NextPage_15);
      Instructions25Components.push(Instructions_25);
      Instructions25Components.push(Two_Back_Example_Stim_2);
      Instructions25Components.push(One_Back_Example_Stim_3);
      Instructions25Components.push(Example_Stim_4);
      Instructions25Components.push(Example_Match_4);
      Instructions25Components.push(Example_No_Match_4);
      
      Instructions25Components.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function Instructions25RoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'Instructions25' ---
      // get current time
      t = Instructions25Clock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *NextPage_15* updates
      if (t >= 0.0 && NextPage_15.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        NextPage_15.tStart = t;  // (not accounting for frame time here)
        NextPage_15.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { NextPage_15.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { NextPage_15.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { NextPage_15.clearEvents(); });
      }
      
      // if NextPage_15 is active this frame...
      if (NextPage_15.status === PsychoJS.Status.STARTED) {
        let theseKeys = NextPage_15.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _NextPage_15_allKeys = _NextPage_15_allKeys.concat(theseKeys);
        if (_NextPage_15_allKeys.length > 0) {
          NextPage_15.keys = _NextPage_15_allKeys[_NextPage_15_allKeys.length - 1].name;  // just the last key pressed
          NextPage_15.rt = _NextPage_15_allKeys[_NextPage_15_allKeys.length - 1].rt;
          NextPage_15.duration = _NextPage_15_allKeys[_NextPage_15_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      
      // *Instructions_25* updates
      if (t >= 0.0 && Instructions_25.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Instructions_25.tStart = t;  // (not accounting for frame time here)
        Instructions_25.frameNStart = frameN;  // exact frame index
        
        Instructions_25.setAutoDraw(true);
      }
      
      
      // if Instructions_25 is active this frame...
      if (Instructions_25.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Two_Back_Example_Stim_2* updates
      if (t >= 0.0 && Two_Back_Example_Stim_2.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Two_Back_Example_Stim_2.tStart = t;  // (not accounting for frame time here)
        Two_Back_Example_Stim_2.frameNStart = frameN;  // exact frame index
        
        Two_Back_Example_Stim_2.setAutoDraw(true);
      }
      
      
      // if Two_Back_Example_Stim_2 is active this frame...
      if (Two_Back_Example_Stim_2.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *One_Back_Example_Stim_3* updates
      if (t >= 0.0 && One_Back_Example_Stim_3.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        One_Back_Example_Stim_3.tStart = t;  // (not accounting for frame time here)
        One_Back_Example_Stim_3.frameNStart = frameN;  // exact frame index
        
        One_Back_Example_Stim_3.setAutoDraw(true);
      }
      
      
      // if One_Back_Example_Stim_3 is active this frame...
      if (One_Back_Example_Stim_3.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_4* updates
      if (t >= 0 && Example_Stim_4.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_4.tStart = t;  // (not accounting for frame time here)
        Example_Stim_4.frameNStart = frameN;  // exact frame index
        
        Example_Stim_4.setAutoDraw(true);
      }
      
      
      // if Example_Stim_4 is active this frame...
      if (Example_Stim_4.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Match_4* updates
      if (t >= 0 && Example_Match_4.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Match_4.tStart = t;  // (not accounting for frame time here)
        Example_Match_4.frameNStart = frameN;  // exact frame index
        
        Example_Match_4.setAutoDraw(true);
      }
      
      
      // if Example_Match_4 is active this frame...
      if (Example_Match_4.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_No_Match_4* updates
      if (t >= 0 && Example_No_Match_4.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_No_Match_4.tStart = t;  // (not accounting for frame time here)
        Example_No_Match_4.frameNStart = frameN;  // exact frame index
        
        Example_No_Match_4.setAutoDraw(true);
      }
      
      
      // if Example_No_Match_4 is active this frame...
      if (Example_No_Match_4.status === PsychoJS.Status.STARTED) {
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      Instructions25Components.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function Instructions25RoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'Instructions25' ---
      Instructions25Components.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('Instructions25.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(NextPage_15.corr, level);
      }
      psychoJS.experiment.addData('NextPage_15.keys', NextPage_15.keys);
      if (typeof NextPage_15.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('NextPage_15.rt', NextPage_15.rt);
          psychoJS.experiment.addData('NextPage_15.duration', NextPage_15.duration);
          routineTimer.reset();
          }
      
      NextPage_15.stop();
      // the Routine "Instructions25" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var Instructions15MaxDurationReached;
var _NextPage_16_allKeys;
var Instructions15MaxDuration;
var Instructions15Components;
function Instructions15RoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'Instructions15' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      Instructions15Clock.reset();
      routineTimer.reset();
      Instructions15MaxDurationReached = false;
      // update component parameters for each repeat
      NextPage_16.keys = undefined;
      NextPage_16.rt = undefined;
      _NextPage_16_allKeys = [];
      psychoJS.experiment.addData('Instructions15.started', globalClock.getTime());
      Instructions15MaxDuration = null
      // keep track of which components have finished
      Instructions15Components = [];
      Instructions15Components.push(NextPage_16);
      Instructions15Components.push(Instructions_15);
      
      Instructions15Components.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function Instructions15RoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'Instructions15' ---
      // get current time
      t = Instructions15Clock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *NextPage_16* updates
      if (t >= 0.0 && NextPage_16.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        NextPage_16.tStart = t;  // (not accounting for frame time here)
        NextPage_16.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { NextPage_16.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { NextPage_16.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { NextPage_16.clearEvents(); });
      }
      
      // if NextPage_16 is active this frame...
      if (NextPage_16.status === PsychoJS.Status.STARTED) {
        let theseKeys = NextPage_16.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _NextPage_16_allKeys = _NextPage_16_allKeys.concat(theseKeys);
        if (_NextPage_16_allKeys.length > 0) {
          NextPage_16.keys = _NextPage_16_allKeys[_NextPage_16_allKeys.length - 1].name;  // just the last key pressed
          NextPage_16.rt = _NextPage_16_allKeys[_NextPage_16_allKeys.length - 1].rt;
          NextPage_16.duration = _NextPage_16_allKeys[_NextPage_16_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      
      // *Instructions_15* updates
      if (t >= 0.0 && Instructions_15.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Instructions_15.tStart = t;  // (not accounting for frame time here)
        Instructions_15.frameNStart = frameN;  // exact frame index
        
        Instructions_15.setAutoDraw(true);
      }
      
      
      // if Instructions_15 is active this frame...
      if (Instructions_15.status === PsychoJS.Status.STARTED) {
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      Instructions15Components.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function Instructions15RoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'Instructions15' ---
      Instructions15Components.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('Instructions15.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(NextPage_16.corr, level);
      }
      psychoJS.experiment.addData('NextPage_16.keys', NextPage_16.keys);
      if (typeof NextPage_16.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('NextPage_16.rt', NextPage_16.rt);
          psychoJS.experiment.addData('NextPage_16.duration', NextPage_16.duration);
          routineTimer.reset();
          }
      
      NextPage_16.stop();
      // the Routine "Instructions15" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var Instructions32MaxDurationReached;
var _NextPage_17_allKeys;
var Instructions32MaxDuration;
var Instructions32Components;
function Instructions32RoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'Instructions32' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      Instructions32Clock.reset();
      routineTimer.reset();
      Instructions32MaxDurationReached = false;
      // update component parameters for each repeat
      NextPage_17.keys = undefined;
      NextPage_17.rt = undefined;
      _NextPage_17_allKeys = [];
      psychoJS.experiment.addData('Instructions32.started', globalClock.getTime());
      Instructions32MaxDuration = null
      // keep track of which components have finished
      Instructions32Components = [];
      Instructions32Components.push(NextPage_17);
      Instructions32Components.push(Instructions_32);
      Instructions32Components.push(Example_Stim_5);
      Instructions32Components.push(Example_Stim_Match_3);
      Instructions32Components.push(Example_Stim_No_Match_3);
      
      Instructions32Components.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function Instructions32RoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'Instructions32' ---
      // get current time
      t = Instructions32Clock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *NextPage_17* updates
      if (t >= 0.0 && NextPage_17.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        NextPage_17.tStart = t;  // (not accounting for frame time here)
        NextPage_17.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { NextPage_17.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { NextPage_17.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { NextPage_17.clearEvents(); });
      }
      
      // if NextPage_17 is active this frame...
      if (NextPage_17.status === PsychoJS.Status.STARTED) {
        let theseKeys = NextPage_17.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _NextPage_17_allKeys = _NextPage_17_allKeys.concat(theseKeys);
        if (_NextPage_17_allKeys.length > 0) {
          NextPage_17.keys = _NextPage_17_allKeys[_NextPage_17_allKeys.length - 1].name;  // just the last key pressed
          NextPage_17.rt = _NextPage_17_allKeys[_NextPage_17_allKeys.length - 1].rt;
          NextPage_17.duration = _NextPage_17_allKeys[_NextPage_17_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      
      // *Instructions_32* updates
      if (t >= 0.0 && Instructions_32.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Instructions_32.tStart = t;  // (not accounting for frame time here)
        Instructions_32.frameNStart = frameN;  // exact frame index
        
        Instructions_32.setAutoDraw(true);
      }
      
      
      // if Instructions_32 is active this frame...
      if (Instructions_32.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_5* updates
      if (t >= 0 && Example_Stim_5.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_5.tStart = t;  // (not accounting for frame time here)
        Example_Stim_5.frameNStart = frameN;  // exact frame index
        
        Example_Stim_5.setAutoDraw(true);
      }
      
      
      // if Example_Stim_5 is active this frame...
      if (Example_Stim_5.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_Match_3* updates
      if (t >= 0 && Example_Stim_Match_3.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_Match_3.tStart = t;  // (not accounting for frame time here)
        Example_Stim_Match_3.frameNStart = frameN;  // exact frame index
        
        Example_Stim_Match_3.setAutoDraw(true);
      }
      
      
      // if Example_Stim_Match_3 is active this frame...
      if (Example_Stim_Match_3.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_No_Match_3* updates
      if (t >= 0 && Example_Stim_No_Match_3.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_No_Match_3.tStart = t;  // (not accounting for frame time here)
        Example_Stim_No_Match_3.frameNStart = frameN;  // exact frame index
        
        Example_Stim_No_Match_3.setAutoDraw(true);
      }
      
      
      // if Example_Stim_No_Match_3 is active this frame...
      if (Example_Stim_No_Match_3.status === PsychoJS.Status.STARTED) {
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      Instructions32Components.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function Instructions32RoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'Instructions32' ---
      Instructions32Components.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('Instructions32.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(NextPage_17.corr, level);
      }
      psychoJS.experiment.addData('NextPage_17.keys', NextPage_17.keys);
      if (typeof NextPage_17.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('NextPage_17.rt', NextPage_17.rt);
          psychoJS.experiment.addData('NextPage_17.duration', NextPage_17.duration);
          routineTimer.reset();
          }
      
      NextPage_17.stop();
      // the Routine "Instructions32" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var Instructions27MaxDurationReached;
var _NextPage_18_allKeys;
var Instructions27MaxDuration;
var Instructions27Components;
function Instructions27RoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'Instructions27' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      Instructions27Clock.reset();
      routineTimer.reset();
      Instructions27MaxDurationReached = false;
      // update component parameters for each repeat
      NextPage_18.keys = undefined;
      NextPage_18.rt = undefined;
      _NextPage_18_allKeys = [];
      psychoJS.experiment.addData('Instructions27.started', globalClock.getTime());
      Instructions27MaxDuration = null
      // keep track of which components have finished
      Instructions27Components = [];
      Instructions27Components.push(NextPage_18);
      Instructions27Components.push(Instructions_27);
      Instructions27Components.push(Example_Stim_6);
      Instructions27Components.push(Example_Stim_Match);
      Instructions27Components.push(Example_Stim_No_Match);
      
      Instructions27Components.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function Instructions27RoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'Instructions27' ---
      // get current time
      t = Instructions27Clock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *NextPage_18* updates
      if (t >= 0.0 && NextPage_18.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        NextPage_18.tStart = t;  // (not accounting for frame time here)
        NextPage_18.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { NextPage_18.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { NextPage_18.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { NextPage_18.clearEvents(); });
      }
      
      // if NextPage_18 is active this frame...
      if (NextPage_18.status === PsychoJS.Status.STARTED) {
        let theseKeys = NextPage_18.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _NextPage_18_allKeys = _NextPage_18_allKeys.concat(theseKeys);
        if (_NextPage_18_allKeys.length > 0) {
          NextPage_18.keys = _NextPage_18_allKeys[_NextPage_18_allKeys.length - 1].name;  // just the last key pressed
          NextPage_18.rt = _NextPage_18_allKeys[_NextPage_18_allKeys.length - 1].rt;
          NextPage_18.duration = _NextPage_18_allKeys[_NextPage_18_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      
      // *Instructions_27* updates
      if (t >= 0.0 && Instructions_27.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Instructions_27.tStart = t;  // (not accounting for frame time here)
        Instructions_27.frameNStart = frameN;  // exact frame index
        
        Instructions_27.setAutoDraw(true);
      }
      
      
      // if Instructions_27 is active this frame...
      if (Instructions_27.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_6* updates
      if (t >= 0 && Example_Stim_6.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_6.tStart = t;  // (not accounting for frame time here)
        Example_Stim_6.frameNStart = frameN;  // exact frame index
        
        Example_Stim_6.setAutoDraw(true);
      }
      
      
      // if Example_Stim_6 is active this frame...
      if (Example_Stim_6.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_Match* updates
      if (t >= 0 && Example_Stim_Match.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_Match.tStart = t;  // (not accounting for frame time here)
        Example_Stim_Match.frameNStart = frameN;  // exact frame index
        
        Example_Stim_Match.setAutoDraw(true);
      }
      
      
      // if Example_Stim_Match is active this frame...
      if (Example_Stim_Match.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_No_Match* updates
      if (t >= 0 && Example_Stim_No_Match.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_No_Match.tStart = t;  // (not accounting for frame time here)
        Example_Stim_No_Match.frameNStart = frameN;  // exact frame index
        
        Example_Stim_No_Match.setAutoDraw(true);
      }
      
      
      // if Example_Stim_No_Match is active this frame...
      if (Example_Stim_No_Match.status === PsychoJS.Status.STARTED) {
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      Instructions27Components.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function Instructions27RoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'Instructions27' ---
      Instructions27Components.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('Instructions27.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(NextPage_18.corr, level);
      }
      psychoJS.experiment.addData('NextPage_18.keys', NextPage_18.keys);
      if (typeof NextPage_18.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('NextPage_18.rt', NextPage_18.rt);
          psychoJS.experiment.addData('NextPage_18.duration', NextPage_18.duration);
          routineTimer.reset();
          }
      
      NextPage_18.stop();
      // the Routine "Instructions27" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var Instructions33MaxDurationReached;
var _NextPage_19_allKeys;
var Instructions33MaxDuration;
var Instructions33Components;
function Instructions33RoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'Instructions33' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      Instructions33Clock.reset();
      routineTimer.reset();
      Instructions33MaxDurationReached = false;
      // update component parameters for each repeat
      NextPage_19.keys = undefined;
      NextPage_19.rt = undefined;
      _NextPage_19_allKeys = [];
      psychoJS.experiment.addData('Instructions33.started', globalClock.getTime());
      Instructions33MaxDuration = null
      // keep track of which components have finished
      Instructions33Components = [];
      Instructions33Components.push(NextPage_19);
      Instructions33Components.push(Instructions_33);
      Instructions33Components.push(Example_Stim_7);
      Instructions33Components.push(Example_Stim_Match_4);
      Instructions33Components.push(Example_Stim_No_Match_4);
      
      Instructions33Components.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function Instructions33RoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'Instructions33' ---
      // get current time
      t = Instructions33Clock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *NextPage_19* updates
      if (t >= 0.0 && NextPage_19.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        NextPage_19.tStart = t;  // (not accounting for frame time here)
        NextPage_19.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { NextPage_19.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { NextPage_19.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { NextPage_19.clearEvents(); });
      }
      
      // if NextPage_19 is active this frame...
      if (NextPage_19.status === PsychoJS.Status.STARTED) {
        let theseKeys = NextPage_19.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _NextPage_19_allKeys = _NextPage_19_allKeys.concat(theseKeys);
        if (_NextPage_19_allKeys.length > 0) {
          NextPage_19.keys = _NextPage_19_allKeys[_NextPage_19_allKeys.length - 1].name;  // just the last key pressed
          NextPage_19.rt = _NextPage_19_allKeys[_NextPage_19_allKeys.length - 1].rt;
          NextPage_19.duration = _NextPage_19_allKeys[_NextPage_19_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      
      // *Instructions_33* updates
      if (t >= 0.0 && Instructions_33.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Instructions_33.tStart = t;  // (not accounting for frame time here)
        Instructions_33.frameNStart = frameN;  // exact frame index
        
        Instructions_33.setAutoDraw(true);
      }
      
      
      // if Instructions_33 is active this frame...
      if (Instructions_33.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_7* updates
      if (t >= 0 && Example_Stim_7.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_7.tStart = t;  // (not accounting for frame time here)
        Example_Stim_7.frameNStart = frameN;  // exact frame index
        
        Example_Stim_7.setAutoDraw(true);
      }
      
      
      // if Example_Stim_7 is active this frame...
      if (Example_Stim_7.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_Match_4* updates
      if (t >= 0 && Example_Stim_Match_4.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_Match_4.tStart = t;  // (not accounting for frame time here)
        Example_Stim_Match_4.frameNStart = frameN;  // exact frame index
        
        Example_Stim_Match_4.setAutoDraw(true);
      }
      
      
      // if Example_Stim_Match_4 is active this frame...
      if (Example_Stim_Match_4.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_No_Match_4* updates
      if (t >= 0 && Example_Stim_No_Match_4.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_No_Match_4.tStart = t;  // (not accounting for frame time here)
        Example_Stim_No_Match_4.frameNStart = frameN;  // exact frame index
        
        Example_Stim_No_Match_4.setAutoDraw(true);
      }
      
      
      // if Example_Stim_No_Match_4 is active this frame...
      if (Example_Stim_No_Match_4.status === PsychoJS.Status.STARTED) {
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      Instructions33Components.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function Instructions33RoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'Instructions33' ---
      Instructions33Components.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('Instructions33.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(NextPage_19.corr, level);
      }
      psychoJS.experiment.addData('NextPage_19.keys', NextPage_19.keys);
      if (typeof NextPage_19.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('NextPage_19.rt', NextPage_19.rt);
          psychoJS.experiment.addData('NextPage_19.duration', NextPage_19.duration);
          routineTimer.reset();
          }
      
      NextPage_19.stop();
      // the Routine "Instructions33" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var Instructions26MaxDurationReached;
var _NextPage_20_allKeys;
var Instructions26MaxDuration;
var Instructions26Components;
function Instructions26RoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'Instructions26' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      Instructions26Clock.reset();
      routineTimer.reset();
      Instructions26MaxDurationReached = false;
      // update component parameters for each repeat
      NextPage_20.keys = undefined;
      NextPage_20.rt = undefined;
      _NextPage_20_allKeys = [];
      psychoJS.experiment.addData('Instructions26.started', globalClock.getTime());
      Instructions26MaxDuration = null
      // keep track of which components have finished
      Instructions26Components = [];
      Instructions26Components.push(NextPage_20);
      Instructions26Components.push(Instructions_26);
      Instructions26Components.push(One_Back_Example_Stim_4);
      Instructions26Components.push(Example_Stim_8);
      Instructions26Components.push(Example_Stim_Match_2);
      Instructions26Components.push(Example_Stim_No_Match_2);
      
      Instructions26Components.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function Instructions26RoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'Instructions26' ---
      // get current time
      t = Instructions26Clock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *NextPage_20* updates
      if (t >= 0.0 && NextPage_20.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        NextPage_20.tStart = t;  // (not accounting for frame time here)
        NextPage_20.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { NextPage_20.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { NextPage_20.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { NextPage_20.clearEvents(); });
      }
      
      // if NextPage_20 is active this frame...
      if (NextPage_20.status === PsychoJS.Status.STARTED) {
        let theseKeys = NextPage_20.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _NextPage_20_allKeys = _NextPage_20_allKeys.concat(theseKeys);
        if (_NextPage_20_allKeys.length > 0) {
          NextPage_20.keys = _NextPage_20_allKeys[_NextPage_20_allKeys.length - 1].name;  // just the last key pressed
          NextPage_20.rt = _NextPage_20_allKeys[_NextPage_20_allKeys.length - 1].rt;
          NextPage_20.duration = _NextPage_20_allKeys[_NextPage_20_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      
      // *Instructions_26* updates
      if (t >= 0.0 && Instructions_26.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Instructions_26.tStart = t;  // (not accounting for frame time here)
        Instructions_26.frameNStart = frameN;  // exact frame index
        
        Instructions_26.setAutoDraw(true);
      }
      
      
      // if Instructions_26 is active this frame...
      if (Instructions_26.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *One_Back_Example_Stim_4* updates
      if (t >= 0.0 && One_Back_Example_Stim_4.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        One_Back_Example_Stim_4.tStart = t;  // (not accounting for frame time here)
        One_Back_Example_Stim_4.frameNStart = frameN;  // exact frame index
        
        One_Back_Example_Stim_4.setAutoDraw(true);
      }
      
      
      // if One_Back_Example_Stim_4 is active this frame...
      if (One_Back_Example_Stim_4.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_8* updates
      if (t >= 0 && Example_Stim_8.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_8.tStart = t;  // (not accounting for frame time here)
        Example_Stim_8.frameNStart = frameN;  // exact frame index
        
        Example_Stim_8.setAutoDraw(true);
      }
      
      
      // if Example_Stim_8 is active this frame...
      if (Example_Stim_8.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_Match_2* updates
      if (t >= 0 && Example_Stim_Match_2.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_Match_2.tStart = t;  // (not accounting for frame time here)
        Example_Stim_Match_2.frameNStart = frameN;  // exact frame index
        
        Example_Stim_Match_2.setAutoDraw(true);
      }
      
      
      // if Example_Stim_Match_2 is active this frame...
      if (Example_Stim_Match_2.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_No_Match_2* updates
      if (t >= 0 && Example_Stim_No_Match_2.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_No_Match_2.tStart = t;  // (not accounting for frame time here)
        Example_Stim_No_Match_2.frameNStart = frameN;  // exact frame index
        
        Example_Stim_No_Match_2.setAutoDraw(true);
      }
      
      
      // if Example_Stim_No_Match_2 is active this frame...
      if (Example_Stim_No_Match_2.status === PsychoJS.Status.STARTED) {
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      Instructions26Components.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function Instructions26RoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'Instructions26' ---
      Instructions26Components.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('Instructions26.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(NextPage_20.corr, level);
      }
      psychoJS.experiment.addData('NextPage_20.keys', NextPage_20.keys);
      if (typeof NextPage_20.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('NextPage_20.rt', NextPage_20.rt);
          psychoJS.experiment.addData('NextPage_20.duration', NextPage_20.duration);
          routineTimer.reset();
          }
      
      NextPage_20.stop();
      // the Routine "Instructions26" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var Instructions34MaxDurationReached;
var _NextPage_21_allKeys;
var Instructions34MaxDuration;
var Instructions34Components;
function Instructions34RoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'Instructions34' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      Instructions34Clock.reset();
      routineTimer.reset();
      Instructions34MaxDurationReached = false;
      // update component parameters for each repeat
      NextPage_21.keys = undefined;
      NextPage_21.rt = undefined;
      _NextPage_21_allKeys = [];
      psychoJS.experiment.addData('Instructions34.started', globalClock.getTime());
      Instructions34MaxDuration = null
      // keep track of which components have finished
      Instructions34Components = [];
      Instructions34Components.push(NextPage_21);
      Instructions34Components.push(Instructions);
      Instructions34Components.push(Example_Stim_9);
      Instructions34Components.push(Example_Stim_Match_5);
      Instructions34Components.push(Example_Stim_No_Match_5);
      
      Instructions34Components.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function Instructions34RoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'Instructions34' ---
      // get current time
      t = Instructions34Clock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *NextPage_21* updates
      if (t >= 0.0 && NextPage_21.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        NextPage_21.tStart = t;  // (not accounting for frame time here)
        NextPage_21.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { NextPage_21.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { NextPage_21.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { NextPage_21.clearEvents(); });
      }
      
      // if NextPage_21 is active this frame...
      if (NextPage_21.status === PsychoJS.Status.STARTED) {
        let theseKeys = NextPage_21.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _NextPage_21_allKeys = _NextPage_21_allKeys.concat(theseKeys);
        if (_NextPage_21_allKeys.length > 0) {
          NextPage_21.keys = _NextPage_21_allKeys[_NextPage_21_allKeys.length - 1].name;  // just the last key pressed
          NextPage_21.rt = _NextPage_21_allKeys[_NextPage_21_allKeys.length - 1].rt;
          NextPage_21.duration = _NextPage_21_allKeys[_NextPage_21_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      
      // *Instructions* updates
      if (t >= 0.0 && Instructions.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Instructions.tStart = t;  // (not accounting for frame time here)
        Instructions.frameNStart = frameN;  // exact frame index
        
        Instructions.setAutoDraw(true);
      }
      
      
      // if Instructions is active this frame...
      if (Instructions.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_9* updates
      if (t >= 0 && Example_Stim_9.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_9.tStart = t;  // (not accounting for frame time here)
        Example_Stim_9.frameNStart = frameN;  // exact frame index
        
        Example_Stim_9.setAutoDraw(true);
      }
      
      
      // if Example_Stim_9 is active this frame...
      if (Example_Stim_9.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_Match_5* updates
      if (t >= 0 && Example_Stim_Match_5.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_Match_5.tStart = t;  // (not accounting for frame time here)
        Example_Stim_Match_5.frameNStart = frameN;  // exact frame index
        
        Example_Stim_Match_5.setAutoDraw(true);
      }
      
      
      // if Example_Stim_Match_5 is active this frame...
      if (Example_Stim_Match_5.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_No_Match_5* updates
      if (t >= 0 && Example_Stim_No_Match_5.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_No_Match_5.tStart = t;  // (not accounting for frame time here)
        Example_Stim_No_Match_5.frameNStart = frameN;  // exact frame index
        
        Example_Stim_No_Match_5.setAutoDraw(true);
      }
      
      
      // if Example_Stim_No_Match_5 is active this frame...
      if (Example_Stim_No_Match_5.status === PsychoJS.Status.STARTED) {
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      Instructions34Components.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function Instructions34RoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'Instructions34' ---
      Instructions34Components.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('Instructions34.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(NextPage_21.corr, level);
      }
      psychoJS.experiment.addData('NextPage_21.keys', NextPage_21.keys);
      if (typeof NextPage_21.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('NextPage_21.rt', NextPage_21.rt);
          psychoJS.experiment.addData('NextPage_21.duration', NextPage_21.duration);
          routineTimer.reset();
          }
      
      NextPage_21.stop();
      // the Routine "Instructions34" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var Instructions28MaxDurationReached;
var _NextPage_22_allKeys;
var Instructions28MaxDuration;
var Instructions28Components;
function Instructions28RoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'Instructions28' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      Instructions28Clock.reset();
      routineTimer.reset();
      Instructions28MaxDurationReached = false;
      // update component parameters for each repeat
      NextPage_22.keys = undefined;
      NextPage_22.rt = undefined;
      _NextPage_22_allKeys = [];
      psychoJS.experiment.addData('Instructions28.started', globalClock.getTime());
      Instructions28MaxDuration = null
      // keep track of which components have finished
      Instructions28Components = [];
      Instructions28Components.push(NextPage_22);
      Instructions28Components.push(Instructions_28);
      Instructions28Components.push(Two_Back_Example_Stim_3);
      Instructions28Components.push(One_Back_Example_Stim_5);
      Instructions28Components.push(Example_Stim_10);
      Instructions28Components.push(Example_Stim_Match_6);
      Instructions28Components.push(Example_Stim_No_Match_6);
      
      Instructions28Components.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function Instructions28RoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'Instructions28' ---
      // get current time
      t = Instructions28Clock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *NextPage_22* updates
      if (t >= 0.0 && NextPage_22.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        NextPage_22.tStart = t;  // (not accounting for frame time here)
        NextPage_22.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { NextPage_22.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { NextPage_22.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { NextPage_22.clearEvents(); });
      }
      
      // if NextPage_22 is active this frame...
      if (NextPage_22.status === PsychoJS.Status.STARTED) {
        let theseKeys = NextPage_22.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _NextPage_22_allKeys = _NextPage_22_allKeys.concat(theseKeys);
        if (_NextPage_22_allKeys.length > 0) {
          NextPage_22.keys = _NextPage_22_allKeys[_NextPage_22_allKeys.length - 1].name;  // just the last key pressed
          NextPage_22.rt = _NextPage_22_allKeys[_NextPage_22_allKeys.length - 1].rt;
          NextPage_22.duration = _NextPage_22_allKeys[_NextPage_22_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      
      // *Instructions_28* updates
      if (t >= 0.0 && Instructions_28.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Instructions_28.tStart = t;  // (not accounting for frame time here)
        Instructions_28.frameNStart = frameN;  // exact frame index
        
        Instructions_28.setAutoDraw(true);
      }
      
      
      // if Instructions_28 is active this frame...
      if (Instructions_28.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Two_Back_Example_Stim_3* updates
      if (t >= 0.0 && Two_Back_Example_Stim_3.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Two_Back_Example_Stim_3.tStart = t;  // (not accounting for frame time here)
        Two_Back_Example_Stim_3.frameNStart = frameN;  // exact frame index
        
        Two_Back_Example_Stim_3.setAutoDraw(true);
      }
      
      
      // if Two_Back_Example_Stim_3 is active this frame...
      if (Two_Back_Example_Stim_3.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *One_Back_Example_Stim_5* updates
      if (t >= 0.0 && One_Back_Example_Stim_5.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        One_Back_Example_Stim_5.tStart = t;  // (not accounting for frame time here)
        One_Back_Example_Stim_5.frameNStart = frameN;  // exact frame index
        
        One_Back_Example_Stim_5.setAutoDraw(true);
      }
      
      
      // if One_Back_Example_Stim_5 is active this frame...
      if (One_Back_Example_Stim_5.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_10* updates
      if (t >= 0 && Example_Stim_10.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_10.tStart = t;  // (not accounting for frame time here)
        Example_Stim_10.frameNStart = frameN;  // exact frame index
        
        Example_Stim_10.setAutoDraw(true);
      }
      
      
      // if Example_Stim_10 is active this frame...
      if (Example_Stim_10.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_Match_6* updates
      if (t >= 0 && Example_Stim_Match_6.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_Match_6.tStart = t;  // (not accounting for frame time here)
        Example_Stim_Match_6.frameNStart = frameN;  // exact frame index
        
        Example_Stim_Match_6.setAutoDraw(true);
      }
      
      
      // if Example_Stim_Match_6 is active this frame...
      if (Example_Stim_Match_6.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_No_Match_6* updates
      if (t >= 0 && Example_Stim_No_Match_6.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_No_Match_6.tStart = t;  // (not accounting for frame time here)
        Example_Stim_No_Match_6.frameNStart = frameN;  // exact frame index
        
        Example_Stim_No_Match_6.setAutoDraw(true);
      }
      
      
      // if Example_Stim_No_Match_6 is active this frame...
      if (Example_Stim_No_Match_6.status === PsychoJS.Status.STARTED) {
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      Instructions28Components.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function Instructions28RoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'Instructions28' ---
      Instructions28Components.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('Instructions28.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(NextPage_22.corr, level);
      }
      psychoJS.experiment.addData('NextPage_22.keys', NextPage_22.keys);
      if (typeof NextPage_22.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('NextPage_22.rt', NextPage_22.rt);
          psychoJS.experiment.addData('NextPage_22.duration', NextPage_22.duration);
          routineTimer.reset();
          }
      
      NextPage_22.stop();
      // the Routine "Instructions28" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var Instructions29MaxDurationReached;
var _NextPage_23_allKeys;
var Instructions29MaxDuration;
var Instructions29Components;
function Instructions29RoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'Instructions29' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      Instructions29Clock.reset();
      routineTimer.reset();
      Instructions29MaxDurationReached = false;
      // update component parameters for each repeat
      NextPage_23.keys = undefined;
      NextPage_23.rt = undefined;
      _NextPage_23_allKeys = [];
      psychoJS.experiment.addData('Instructions29.started', globalClock.getTime());
      Instructions29MaxDuration = null
      // keep track of which components have finished
      Instructions29Components = [];
      Instructions29Components.push(NextPage_23);
      Instructions29Components.push(Instructions_29);
      Instructions29Components.push(Green_Border_2);
      Instructions29Components.push(Two_Back_Example_Stim_4);
      Instructions29Components.push(One_Back_Example_Stim_6);
      Instructions29Components.push(Example_Stim_11);
      Instructions29Components.push(Example_Stim_Match_7);
      Instructions29Components.push(Example_Stim_No_Match_7);
      
      Instructions29Components.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function Instructions29RoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'Instructions29' ---
      // get current time
      t = Instructions29Clock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *NextPage_23* updates
      if (t >= 0.0 && NextPage_23.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        NextPage_23.tStart = t;  // (not accounting for frame time here)
        NextPage_23.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { NextPage_23.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { NextPage_23.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { NextPage_23.clearEvents(); });
      }
      
      // if NextPage_23 is active this frame...
      if (NextPage_23.status === PsychoJS.Status.STARTED) {
        let theseKeys = NextPage_23.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _NextPage_23_allKeys = _NextPage_23_allKeys.concat(theseKeys);
        if (_NextPage_23_allKeys.length > 0) {
          NextPage_23.keys = _NextPage_23_allKeys[_NextPage_23_allKeys.length - 1].name;  // just the last key pressed
          NextPage_23.rt = _NextPage_23_allKeys[_NextPage_23_allKeys.length - 1].rt;
          NextPage_23.duration = _NextPage_23_allKeys[_NextPage_23_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      
      // *Instructions_29* updates
      if (t >= 0.0 && Instructions_29.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Instructions_29.tStart = t;  // (not accounting for frame time here)
        Instructions_29.frameNStart = frameN;  // exact frame index
        
        Instructions_29.setAutoDraw(true);
      }
      
      
      // if Instructions_29 is active this frame...
      if (Instructions_29.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Green_Border_2* updates
      if (t >= 0.0 && Green_Border_2.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Green_Border_2.tStart = t;  // (not accounting for frame time here)
        Green_Border_2.frameNStart = frameN;  // exact frame index
        
        Green_Border_2.setAutoDraw(true);
      }
      
      
      // if Green_Border_2 is active this frame...
      if (Green_Border_2.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Two_Back_Example_Stim_4* updates
      if (t >= 0.0 && Two_Back_Example_Stim_4.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Two_Back_Example_Stim_4.tStart = t;  // (not accounting for frame time here)
        Two_Back_Example_Stim_4.frameNStart = frameN;  // exact frame index
        
        Two_Back_Example_Stim_4.setAutoDraw(true);
      }
      
      
      // if Two_Back_Example_Stim_4 is active this frame...
      if (Two_Back_Example_Stim_4.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *One_Back_Example_Stim_6* updates
      if (t >= 0.0 && One_Back_Example_Stim_6.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        One_Back_Example_Stim_6.tStart = t;  // (not accounting for frame time here)
        One_Back_Example_Stim_6.frameNStart = frameN;  // exact frame index
        
        One_Back_Example_Stim_6.setAutoDraw(true);
      }
      
      
      // if One_Back_Example_Stim_6 is active this frame...
      if (One_Back_Example_Stim_6.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_11* updates
      if (t >= 0 && Example_Stim_11.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_11.tStart = t;  // (not accounting for frame time here)
        Example_Stim_11.frameNStart = frameN;  // exact frame index
        
        Example_Stim_11.setAutoDraw(true);
      }
      
      
      // if Example_Stim_11 is active this frame...
      if (Example_Stim_11.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_Match_7* updates
      if (t >= 0 && Example_Stim_Match_7.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_Match_7.tStart = t;  // (not accounting for frame time here)
        Example_Stim_Match_7.frameNStart = frameN;  // exact frame index
        
        Example_Stim_Match_7.setAutoDraw(true);
      }
      
      
      // if Example_Stim_Match_7 is active this frame...
      if (Example_Stim_Match_7.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *Example_Stim_No_Match_7* updates
      if (t >= 0 && Example_Stim_No_Match_7.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Example_Stim_No_Match_7.tStart = t;  // (not accounting for frame time here)
        Example_Stim_No_Match_7.frameNStart = frameN;  // exact frame index
        
        Example_Stim_No_Match_7.setAutoDraw(true);
      }
      
      
      // if Example_Stim_No_Match_7 is active this frame...
      if (Example_Stim_No_Match_7.status === PsychoJS.Status.STARTED) {
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      Instructions29Components.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function Instructions29RoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'Instructions29' ---
      Instructions29Components.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('Instructions29.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(NextPage_23.corr, level);
      }
      psychoJS.experiment.addData('NextPage_23.keys', NextPage_23.keys);
      if (typeof NextPage_23.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('NextPage_23.rt', NextPage_23.rt);
          psychoJS.experiment.addData('NextPage_23.duration', NextPage_23.duration);
          routineTimer.reset();
          }
      
      NextPage_23.stop();
      // the Routine "Instructions29" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var Instructions22MaxDurationReached;
var _NextPage_24_allKeys;
var Instructions22MaxDuration;
var Instructions22Components;
function Instructions22RoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'Instructions22' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      Instructions22Clock.reset();
      routineTimer.reset();
      Instructions22MaxDurationReached = false;
      // update component parameters for each repeat
      NextPage_24.keys = undefined;
      NextPage_24.rt = undefined;
      _NextPage_24_allKeys = [];
      psychoJS.experiment.addData('Instructions22.started', globalClock.getTime());
      Instructions22MaxDuration = null
      // keep track of which components have finished
      Instructions22Components = [];
      Instructions22Components.push(NextPage_24);
      Instructions22Components.push(Instructions_22);
      
      Instructions22Components.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function Instructions22RoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'Instructions22' ---
      // get current time
      t = Instructions22Clock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *NextPage_24* updates
      if (t >= 0.0 && NextPage_24.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        NextPage_24.tStart = t;  // (not accounting for frame time here)
        NextPage_24.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { NextPage_24.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { NextPage_24.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { NextPage_24.clearEvents(); });
      }
      
      // if NextPage_24 is active this frame...
      if (NextPage_24.status === PsychoJS.Status.STARTED) {
        let theseKeys = NextPage_24.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _NextPage_24_allKeys = _NextPage_24_allKeys.concat(theseKeys);
        if (_NextPage_24_allKeys.length > 0) {
          NextPage_24.keys = _NextPage_24_allKeys[_NextPage_24_allKeys.length - 1].name;  // just the last key pressed
          NextPage_24.rt = _NextPage_24_allKeys[_NextPage_24_allKeys.length - 1].rt;
          NextPage_24.duration = _NextPage_24_allKeys[_NextPage_24_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      
      // *Instructions_22* updates
      if (t >= 0.0 && Instructions_22.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Instructions_22.tStart = t;  // (not accounting for frame time here)
        Instructions_22.frameNStart = frameN;  // exact frame index
        
        Instructions_22.setAutoDraw(true);
      }
      
      
      // if Instructions_22 is active this frame...
      if (Instructions_22.status === PsychoJS.Status.STARTED) {
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      Instructions22Components.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function Instructions22RoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'Instructions22' ---
      Instructions22Components.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('Instructions22.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(NextPage_24.corr, level);
      }
      psychoJS.experiment.addData('NextPage_24.keys', NextPage_24.keys);
      if (typeof NextPage_24.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('NextPage_24.rt', NextPage_24.rt);
          psychoJS.experiment.addData('NextPage_24.duration', NextPage_24.duration);
          routineTimer.reset();
          }
      
      NextPage_24.stop();
      // the Routine "Instructions22" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var Instructions30MaxDurationReached;
var _NextPage_25_allKeys;
var Instructions30MaxDuration;
var Instructions30Components;
function Instructions30RoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'Instructions30' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      Instructions30Clock.reset();
      routineTimer.reset();
      Instructions30MaxDurationReached = false;
      // update component parameters for each repeat
      NextPage_25.keys = undefined;
      NextPage_25.rt = undefined;
      _NextPage_25_allKeys = [];
      psychoJS.experiment.addData('Instructions30.started', globalClock.getTime());
      Instructions30MaxDuration = null
      // keep track of which components have finished
      Instructions30Components = [];
      Instructions30Components.push(NextPage_25);
      Instructions30Components.push(Instructions_30);
      
      Instructions30Components.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function Instructions30RoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'Instructions30' ---
      // get current time
      t = Instructions30Clock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *NextPage_25* updates
      if (t >= 0.0 && NextPage_25.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        NextPage_25.tStart = t;  // (not accounting for frame time here)
        NextPage_25.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { NextPage_25.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { NextPage_25.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { NextPage_25.clearEvents(); });
      }
      
      // if NextPage_25 is active this frame...
      if (NextPage_25.status === PsychoJS.Status.STARTED) {
        let theseKeys = NextPage_25.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _NextPage_25_allKeys = _NextPage_25_allKeys.concat(theseKeys);
        if (_NextPage_25_allKeys.length > 0) {
          NextPage_25.keys = _NextPage_25_allKeys[_NextPage_25_allKeys.length - 1].name;  // just the last key pressed
          NextPage_25.rt = _NextPage_25_allKeys[_NextPage_25_allKeys.length - 1].rt;
          NextPage_25.duration = _NextPage_25_allKeys[_NextPage_25_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      
      // *Instructions_30* updates
      if (t >= 0.0 && Instructions_30.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Instructions_30.tStart = t;  // (not accounting for frame time here)
        Instructions_30.frameNStart = frameN;  // exact frame index
        
        Instructions_30.setAutoDraw(true);
      }
      
      
      // if Instructions_30 is active this frame...
      if (Instructions_30.status === PsychoJS.Status.STARTED) {
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      Instructions30Components.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function Instructions30RoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'Instructions30' ---
      Instructions30Components.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('Instructions30.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(NextPage_25.corr, level);
      }
      psychoJS.experiment.addData('NextPage_25.keys', NextPage_25.keys);
      if (typeof NextPage_25.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('NextPage_25.rt', NextPage_25.rt);
          psychoJS.experiment.addData('NextPage_25.duration', NextPage_25.duration);
          routineTimer.reset();
          }
      
      NextPage_25.stop();
      // the Routine "Instructions30" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var Instructions36MaxDurationReached;
var _NextPage_26_allKeys;
var Instructions36MaxDuration;
var Instructions36Components;
function Instructions36RoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'Instructions36' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      Instructions36Clock.reset();
      routineTimer.reset();
      Instructions36MaxDurationReached = false;
      // update component parameters for each repeat
      NextPage_26.keys = undefined;
      NextPage_26.rt = undefined;
      _NextPage_26_allKeys = [];
      psychoJS.experiment.addData('Instructions36.started', globalClock.getTime());
      Instructions36MaxDuration = null
      // keep track of which components have finished
      Instructions36Components = [];
      Instructions36Components.push(NextPage_26);
      Instructions36Components.push(Instructions_36);
      
      Instructions36Components.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function Instructions36RoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'Instructions36' ---
      // get current time
      t = Instructions36Clock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *NextPage_26* updates
      if (t >= 0.0 && NextPage_26.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        NextPage_26.tStart = t;  // (not accounting for frame time here)
        NextPage_26.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { NextPage_26.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { NextPage_26.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { NextPage_26.clearEvents(); });
      }
      
      // if NextPage_26 is active this frame...
      if (NextPage_26.status === PsychoJS.Status.STARTED) {
        let theseKeys = NextPage_26.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _NextPage_26_allKeys = _NextPage_26_allKeys.concat(theseKeys);
        if (_NextPage_26_allKeys.length > 0) {
          NextPage_26.keys = _NextPage_26_allKeys[_NextPage_26_allKeys.length - 1].name;  // just the last key pressed
          NextPage_26.rt = _NextPage_26_allKeys[_NextPage_26_allKeys.length - 1].rt;
          NextPage_26.duration = _NextPage_26_allKeys[_NextPage_26_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      
      // *Instructions_36* updates
      if (t >= 0.0 && Instructions_36.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Instructions_36.tStart = t;  // (not accounting for frame time here)
        Instructions_36.frameNStart = frameN;  // exact frame index
        
        Instructions_36.setAutoDraw(true);
      }
      
      
      // if Instructions_36 is active this frame...
      if (Instructions_36.status === PsychoJS.Status.STARTED) {
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      Instructions36Components.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function Instructions36RoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'Instructions36' ---
      Instructions36Components.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('Instructions36.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(NextPage_26.corr, level);
      }
      psychoJS.experiment.addData('NextPage_26.keys', NextPage_26.keys);
      if (typeof NextPage_26.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('NextPage_26.rt', NextPage_26.rt);
          psychoJS.experiment.addData('NextPage_26.duration', NextPage_26.duration);
          routineTimer.reset();
          }
      
      NextPage_26.stop();
      // the Routine "Instructions36" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var PracticeTrial5_CueMaxDurationReached;
var PracticeTrial5_CueMaxDuration;
var PracticeTrial5_CueComponents;
function PracticeTrial5_CueRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'PracticeTrial5_Cue' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      PracticeTrial5_CueClock.reset(routineTimer.getTime());
      routineTimer.add(2.500000);
      PracticeTrial5_CueMaxDurationReached = false;
      // update component parameters for each repeat
      psychoJS.experiment.addData('PracticeTrial5_Cue.started', globalClock.getTime());
      PracticeTrial5_CueMaxDuration = null
      // keep track of which components have finished
      PracticeTrial5_CueComponents = [];
      PracticeTrial5_CueComponents.push(CueFix_5);
      PracticeTrial5_CueComponents.push(Cue_2Back);
      
      PracticeTrial5_CueComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function PracticeTrial5_CueRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'PracticeTrial5_Cue' ---
      // get current time
      t = PracticeTrial5_CueClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *CueFix_5* updates
      if (t >= 0.0 && CueFix_5.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        CueFix_5.tStart = t;  // (not accounting for frame time here)
        CueFix_5.frameNStart = frameN;  // exact frame index
        
        CueFix_5.setAutoDraw(true);
      }
      
      
      // if CueFix_5 is active this frame...
      if (CueFix_5.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (CueFix_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        CueFix_5.tStop = t;  // not accounting for scr refresh
        CueFix_5.frameNStop = frameN;  // exact frame index
        // update status
        CueFix_5.status = PsychoJS.Status.FINISHED;
        CueFix_5.setAutoDraw(false);
      }
      
      
      // *Cue_2Back* updates
      if (t >= 0.5 && Cue_2Back.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Cue_2Back.tStart = t;  // (not accounting for frame time here)
        Cue_2Back.frameNStart = frameN;  // exact frame index
        
        Cue_2Back.setAutoDraw(true);
      }
      
      
      // if Cue_2Back is active this frame...
      if (Cue_2Back.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (Cue_2Back.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        Cue_2Back.tStop = t;  // not accounting for scr refresh
        Cue_2Back.frameNStop = frameN;  // exact frame index
        // update status
        Cue_2Back.status = PsychoJS.Status.FINISHED;
        Cue_2Back.setAutoDraw(false);
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      PracticeTrial5_CueComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function PracticeTrial5_CueRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'PracticeTrial5_Cue' ---
      PracticeTrial5_CueComponents.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('PracticeTrial5_Cue.stopped', globalClock.getTime());
      if (routineForceEnded) {
          routineTimer.reset();} else if (PracticeTrial5_CueMaxDurationReached) {
          PracticeTrial5_CueClock.add(PracticeTrial5_CueMaxDuration);
      } else {
          PracticeTrial5_CueClock.add(2.500000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var PracticeTrial6_CueMaxDurationReached;
var PracticeTrial6_CueMaxDuration;
var PracticeTrial6_CueComponents;
function PracticeTrial6_CueRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'PracticeTrial6_Cue' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      PracticeTrial6_CueClock.reset(routineTimer.getTime());
      routineTimer.add(3.000000);
      PracticeTrial6_CueMaxDurationReached = false;
      // update component parameters for each repeat
      psychoJS.experiment.addData('PracticeTrial6_Cue.started', globalClock.getTime());
      PracticeTrial6_CueMaxDuration = null
      // keep track of which components have finished
      PracticeTrial6_CueComponents = [];
      PracticeTrial6_CueComponents.push(CueFix_6);
      PracticeTrial6_CueComponents.push(CueTarget_6);
      PracticeTrial6_CueComponents.push(CueTargetImage_6);
      
      PracticeTrial6_CueComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function PracticeTrial6_CueRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'PracticeTrial6_Cue' ---
      // get current time
      t = PracticeTrial6_CueClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *CueFix_6* updates
      if (t >= 0.0 && CueFix_6.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        CueFix_6.tStart = t;  // (not accounting for frame time here)
        CueFix_6.frameNStart = frameN;  // exact frame index
        
        CueFix_6.setAutoDraw(true);
      }
      
      
      // if CueFix_6 is active this frame...
      if (CueFix_6.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (CueFix_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        CueFix_6.tStop = t;  // not accounting for scr refresh
        CueFix_6.frameNStop = frameN;  // exact frame index
        // update status
        CueFix_6.status = PsychoJS.Status.FINISHED;
        CueFix_6.setAutoDraw(false);
      }
      
      
      // *CueTarget_6* updates
      if (t >= 0.5 && CueTarget_6.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        CueTarget_6.tStart = t;  // (not accounting for frame time here)
        CueTarget_6.frameNStart = frameN;  // exact frame index
        
        CueTarget_6.setAutoDraw(true);
      }
      
      
      // if CueTarget_6 is active this frame...
      if (CueTarget_6.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.5 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (CueTarget_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        CueTarget_6.tStop = t;  // not accounting for scr refresh
        CueTarget_6.frameNStop = frameN;  // exact frame index
        // update status
        CueTarget_6.status = PsychoJS.Status.FINISHED;
        CueTarget_6.setAutoDraw(false);
      }
      
      
      // *CueTargetImage_6* updates
      if (t >= 0.5 && CueTargetImage_6.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        CueTargetImage_6.tStart = t;  // (not accounting for frame time here)
        CueTargetImage_6.frameNStart = frameN;  // exact frame index
        
        CueTargetImage_6.setAutoDraw(true);
      }
      
      
      // if CueTargetImage_6 is active this frame...
      if (CueTargetImage_6.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.5 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (CueTargetImage_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        CueTargetImage_6.tStop = t;  // not accounting for scr refresh
        CueTargetImage_6.frameNStop = frameN;  // exact frame index
        // update status
        CueTargetImage_6.status = PsychoJS.Status.FINISHED;
        CueTargetImage_6.setAutoDraw(false);
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      PracticeTrial6_CueComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function PracticeTrial6_CueRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'PracticeTrial6_Cue' ---
      PracticeTrial6_CueComponents.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('PracticeTrial6_Cue.stopped', globalClock.getTime());
      if (routineForceEnded) {
          routineTimer.reset();} else if (PracticeTrial6_CueMaxDurationReached) {
          PracticeTrial6_CueClock.add(PracticeTrial6_CueMaxDuration);
      } else {
          PracticeTrial6_CueClock.add(3.000000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var PracticeTrial7_CueMaxDurationReached;
var PracticeTrial7_CueMaxDuration;
var PracticeTrial7_CueComponents;
function PracticeTrial7_CueRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'PracticeTrial7_Cue' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      PracticeTrial7_CueClock.reset(routineTimer.getTime());
      routineTimer.add(2.500000);
      PracticeTrial7_CueMaxDurationReached = false;
      // update component parameters for each repeat
      psychoJS.experiment.addData('PracticeTrial7_Cue.started', globalClock.getTime());
      PracticeTrial7_CueMaxDuration = null
      // keep track of which components have finished
      PracticeTrial7_CueComponents = [];
      PracticeTrial7_CueComponents.push(CueFix_7);
      PracticeTrial7_CueComponents.push(Cue_2Back_2);
      
      PracticeTrial7_CueComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function PracticeTrial7_CueRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'PracticeTrial7_Cue' ---
      // get current time
      t = PracticeTrial7_CueClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *CueFix_7* updates
      if (t >= 0.0 && CueFix_7.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        CueFix_7.tStart = t;  // (not accounting for frame time here)
        CueFix_7.frameNStart = frameN;  // exact frame index
        
        CueFix_7.setAutoDraw(true);
      }
      
      
      // if CueFix_7 is active this frame...
      if (CueFix_7.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (CueFix_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        CueFix_7.tStop = t;  // not accounting for scr refresh
        CueFix_7.frameNStop = frameN;  // exact frame index
        // update status
        CueFix_7.status = PsychoJS.Status.FINISHED;
        CueFix_7.setAutoDraw(false);
      }
      
      
      // *Cue_2Back_2* updates
      if (t >= 0.5 && Cue_2Back_2.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        Cue_2Back_2.tStart = t;  // (not accounting for frame time here)
        Cue_2Back_2.frameNStart = frameN;  // exact frame index
        
        Cue_2Back_2.setAutoDraw(true);
      }
      
      
      // if Cue_2Back_2 is active this frame...
      if (Cue_2Back_2.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (Cue_2Back_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        Cue_2Back_2.tStop = t;  // not accounting for scr refresh
        Cue_2Back_2.frameNStop = frameN;  // exact frame index
        // update status
        Cue_2Back_2.status = PsychoJS.Status.FINISHED;
        Cue_2Back_2.setAutoDraw(false);
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      PracticeTrial7_CueComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function PracticeTrial7_CueRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'PracticeTrial7_Cue' ---
      PracticeTrial7_CueComponents.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('PracticeTrial7_Cue.stopped', globalClock.getTime());
      if (routineForceEnded) {
          routineTimer.reset();} else if (PracticeTrial7_CueMaxDurationReached) {
          PracticeTrial7_CueClock.add(PracticeTrial7_CueMaxDuration);
      } else {
          PracticeTrial7_CueClock.add(2.500000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var PracticeTrial8_CueMaxDurationReached;
var PracticeTrial8_CueMaxDuration;
var PracticeTrial8_CueComponents;
function PracticeTrial8_CueRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'PracticeTrial8_Cue' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      PracticeTrial8_CueClock.reset(routineTimer.getTime());
      routineTimer.add(3.000000);
      PracticeTrial8_CueMaxDurationReached = false;
      // update component parameters for each repeat
      psychoJS.experiment.addData('PracticeTrial8_Cue.started', globalClock.getTime());
      PracticeTrial8_CueMaxDuration = null
      // keep track of which components have finished
      PracticeTrial8_CueComponents = [];
      PracticeTrial8_CueComponents.push(CueFix_8);
      PracticeTrial8_CueComponents.push(CueTarget_8);
      PracticeTrial8_CueComponents.push(CueTargetImage_8);
      
      PracticeTrial8_CueComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
function PracticeTrial8_CueRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'PracticeTrial8_Cue' ---
      // get current time
      t = PracticeTrial8_CueClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *CueFix_8* updates
      if (t >= 0.0 && CueFix_8.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        CueFix_8.tStart = t;  // (not accounting for frame time here)
        CueFix_8.frameNStart = frameN;  // exact frame index
        
        CueFix_8.setAutoDraw(true);
      }
      
      
      // if CueFix_8 is active this frame...
      if (CueFix_8.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (CueFix_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        CueFix_8.tStop = t;  // not accounting for scr refresh
        CueFix_8.frameNStop = frameN;  // exact frame index
        // update status
        CueFix_8.status = PsychoJS.Status.FINISHED;
        CueFix_8.setAutoDraw(false);
      }
      
      
      // *CueTarget_8* updates
      if (t >= 0.5 && CueTarget_8.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        CueTarget_8.tStart = t;  // (not accounting for frame time here)
        CueTarget_8.frameNStart = frameN;  // exact frame index
        
        CueTarget_8.setAutoDraw(true);
      }
      
      
      // if CueTarget_8 is active this frame...
      if (CueTarget_8.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.5 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (CueTarget_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        CueTarget_8.tStop = t;  // not accounting for scr refresh
        CueTarget_8.frameNStop = frameN;  // exact frame index
        // update status
        CueTarget_8.status = PsychoJS.Status.FINISHED;
        CueTarget_8.setAutoDraw(false);
      }
      
      
      // *CueTargetImage_8* updates
      if (t >= 0.5 && CueTargetImage_8.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        CueTargetImage_8.tStart = t;  // (not accounting for frame time here)
        CueTargetImage_8.frameNStart = frameN;  // exact frame index
        
        CueTargetImage_8.setAutoDraw(true);
      }
      
      
      // if CueTargetImage_8 is active this frame...
      if (CueTargetImage_8.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.5 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (CueTargetImage_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        CueTargetImage_8.tStop = t;  // not accounting for scr refresh
        CueTargetImage_8.frameNStop = frameN;  // exact frame index
        // update status
        CueTargetImage_8.status = PsychoJS.Status.FINISHED;
        CueTargetImage_8.setAutoDraw(false);
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      PracticeTrial8_CueComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function PracticeTrial8_CueRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'PracticeTrial8_Cue' ---
      PracticeTrial8_CueComponents.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('PracticeTrial8_Cue.stopped', globalClock.getTime());
      if (routineForceEnded) {
          routineTimer.reset();} else if (PracticeTrial8_CueMaxDurationReached) {
          PracticeTrial8_CueClock.add(PracticeTrial8_CueMaxDuration);
      } else {
          PracticeTrial8_CueClock.add(3.000000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
var GoodbyeMaxDurationReached;
var _EndProgram_allKeys;
var GoodbyeMaxDuration;
var GoodbyeComponents;
function GoodbyeRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'Goodbye' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      GoodbyeClock.reset();
      routineTimer.reset();
      GoodbyeMaxDurationReached = false;
      // update component parameters for each repeat
      EndProgram.keys = undefined;
      EndProgram.rt = undefined;
      _EndProgram_allKeys = [];
      psychoJS.experiment.addData('Goodbye.started', globalClock.getTime());
      GoodbyeMaxDuration = null
      // keep track of which components have finished
      GoodbyeComponents = [];
      GoodbyeComponents.push(EndProgram);
      GoodbyeComponents.push(AllDone);
      
      GoodbyeComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
         });
      return Scheduler.Event.NEXT;
    }
  }
  
  
var _pj;
function GoodbyeRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'Goodbye' ---
      // get current time
      t = GoodbyeClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *EndProgram* updates
      if (t >= 0.0 && EndProgram.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        EndProgram.tStart = t;  // (not accounting for frame time here)
        EndProgram.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { EndProgram.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { EndProgram.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { EndProgram.clearEvents(); });
      }
      
      // if EndProgram is active this frame...
      if (EndProgram.status === PsychoJS.Status.STARTED) {
        let theseKeys = EndProgram.getKeys({
          keyList: typeof ['space','escape'] === 'string' ? [['space','escape']] : ['space','escape'], 
          waitRelease: false
        });
        _EndProgram_allKeys = _EndProgram_allKeys.concat(theseKeys);
        if (_EndProgram_allKeys.length > 0) {
          EndProgram.keys = _EndProgram_allKeys[_EndProgram_allKeys.length - 1].name;  // just the last key pressed
          EndProgram.rt = _EndProgram_allKeys[_EndProgram_allKeys.length - 1].rt;
          EndProgram.duration = _EndProgram_allKeys[_EndProgram_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      // Run 'Each Frame' code from code
      var _pj;
      function _pj_snippets(container) {
          function in_es6(left, right) {
              if (((right instanceof Array) || ((typeof right) === "string"))) {
                  return (right.indexOf(left) > (- 1));
              } else {
                  if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                      return right.has(left);
                  } else {
                      return (left in right);
                  }
              }
          }
          container["in_es6"] = in_es6;
          return container;
      }
      _pj = {};
      _pj_snippets(_pj);
      if (_pj.in_es6("space", key_resp.keys)) {
          core.quit();
      }
      
      
      // *AllDone* updates
      if (t >= 0.0 && AllDone.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        AllDone.tStart = t;  // (not accounting for frame time here)
        AllDone.frameNStart = frameN;  // exact frame index
        
        AllDone.setAutoDraw(true);
      }
      
      
      // if AllDone is active this frame...
      if (AllDone.status === PsychoJS.Status.STARTED) {
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      GoodbyeComponents.forEach( function(thisComponent) {
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
        }
      });
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  
function GoodbyeRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'Goodbye' ---
      GoodbyeComponents.forEach( function(thisComponent) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      });
      psychoJS.experiment.addData('Goodbye.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(EndProgram.corr, level);
      }
      psychoJS.experiment.addData('EndProgram.keys', EndProgram.keys);
      if (typeof EndProgram.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('EndProgram.rt', EndProgram.rt);
          psychoJS.experiment.addData('EndProgram.duration', EndProgram.duration);
          routineTimer.reset();
          }
      
      EndProgram.stop();
      // the Routine "Goodbye" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  
function importConditions(currentLoop) {
    return async function () {
      psychoJS.importAttributes(currentLoop.getCurrentTrial());
      return Scheduler.Event.NEXT;
      };
  }
  
  
async function quitPsychoJS(message, isCompleted) {
    // Check for and save orphaned data
    if (psychoJS.experiment.isEntryEmpty()) {
      psychoJS.experiment.nextEntry();
    }
    psychoJS.window.close();
    psychoJS.quit({message: message, isCompleted: isCompleted});
    
    return Scheduler.Event.QUIT;
  }
