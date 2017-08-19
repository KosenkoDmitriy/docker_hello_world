if (Meteor.isClient) {
    // Connect to Django DDP service
    // Django = DDP.connect('http://'+window.location.hostname+':8000/');
    //Django = DDP.connect('http://127.0.0.1:8000/');
    // Create local collections for Django models received via DDP
    //Tasks = new Mongo.Collection("JON.program", {connection: Django});

    // This code only runs on the client
    options = {};
    if (__meteor_runtime_config__.hasOwnProperty('DDP_DEFAULT_CONNECTION_URL')) {
        Django = Meteor;
    } else {
        Django = DDP.connect(window.location.protocol + '//'+window.location.hostname+':8000/');
        options.connection = Django;
    }
    Programs = new Mongo.Collection("JON.program", options);
    ProgramSub = Django.subscribe('Programs');

    Template.body.helpers({
      tasks: function () {
          return Programs.find({});
      }
      //   tasks: [
      //       { name: "Program 1" },
      //       { name: "Program 2" },
      //       { name: "Program 3" },
      //   ]
    });

}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });
}
