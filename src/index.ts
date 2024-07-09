import { JupyterFrontEnd, JupyterFrontEndPlugin } from '@jupyterlab/application'; 
import { ILauncher } from '@jupyterlab/launcher';
import { PageConfig } from '@jupyterlab/coreutils';

import '../style/index.css';


function addLauncherShortcuts(shortcutsData: any, launcher: ILauncher, app: JupyterFrontEnd) {
    for (let shortcut of shortcutsData.shortcuts) {

      let commandId = 'shortcut:' + shortcut.name;

      app.commands.addCommand(commandId, {
        label: shortcut.title,
        execute: () => {
          window.open(shortcut.target, '_blank');
        }
      });
      let command : ILauncher.IItemOptions = {
        command: commandId,
        category: 'Notebook'
      };
      if (shortcut.icon_url) {
        command.kernelIconUrl =  shortcut.icon_url;
      }
      launcher.add(command);
    }
}
/**
 * Initialization data for the jupyterlab-server-proxy extension.
 */
const extension: JupyterFrontEndPlugin<void> = {
  id: 'jupyterlab-launcher-shortcuts',
  autoStart: true,
  requires: [ILauncher],
  activate: (app: JupyterFrontEnd, launcher: ILauncher) => {
    // FIXME: What the callback hell is this
    fetch(PageConfig.getBaseUrl() + 'launcher-shortcuts/shortcuts').then(
      response => {
        if (!response.ok) {
          console.log('Fetching metadata about shortcuts failed. Make sure jupyter-launcher-shortcuts is installed');
          console.log(response);
        } else {
          response.json().then(data => addLauncherShortcuts(data, launcher, app))
        }

      }
    )
  }
};

export default extension;
