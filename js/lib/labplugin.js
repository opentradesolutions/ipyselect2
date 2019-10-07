var ipyselect2 = require('./index');
var base = require('@jupyter-widgets/base');

module.exports = {
  id: 'ipyselect2',
  requires: [base.IJupyterWidgetRegistry],
  activate: function(app, widgets) {
      widgets.registerWidget({
          name: 'ipyselect2',
          version: ipyselect2.version,
          exports: ipyselect2
      });
  },
  autoStart: true
};

