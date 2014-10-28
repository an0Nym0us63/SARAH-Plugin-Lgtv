exports.action = function(data, callback, config, SARAH){
config = config.modules.lgtv;
if (!config.ip){
		console.log("La variable url n'est pas configurée");
		return callback({'tts' : "La variable adresse n'est pas configurée"})};
if (!config.key){
		key='0000'
}
else{
	key=config.key;
	}
	if (data.ok=='yes'){
		execprocess(data.lgtv);
		pause(3000);
		execprocess("20");
		}
	else {if (typeof data.beaucoup=='string'){
			execprocess(data.lgtv);
			pause(500);
			execprocess(data.lgtv);
			pause(500);
			execprocess(data.lgtv);
			pause(500);
			execprocess(data.lgtv);
			pause(500);
			execprocess(data.lgtv);
			}
 	else {if (data.chaine=="yes" && typeof data.lgtv2 === 'undefined'){
			execprocess(data.lgtv);
			pause(500);
			execprocess("20");
			}
		  else {if (data.chaine=="yes" && typeof data.lgtv2 === 'string'){
				execprocess(data.lgtv);
				pause(500);
				execprocess(data.lgtv2);
				pause(500);
				execprocess("20");
				}
				else{
					execprocess(data.lgtv);
				}
			}
		}
		}
	callback({ 'tts': ""});

function pause(millis){
	var date = new Date();
	var curDate = null;
	do { curDate = new Date(); }
	while(curDate-date < millis);
	};
	
function execprocess(command){
	var exec = require('child_process').exec;
	var process = __dirname+'\\lib\\lg.py '+command+' '+config.ip+' '+key;
	var child = exec(process,
	function (error, stdout, stderr) {
	})};
};