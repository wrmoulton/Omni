# USD Explorer App Template

![USD Explorer Hero Image](../../../readme-assets/usd_explorer.jpg)

**Based On:** `Omniverse Kit SDK 106.0`

## Overview

The USD Explorer App Template is designed to provide a robust starting point for developers looking to visualize and interact with large-scale environments such as factories, warehouses, and other expansive scenes using Open Universal Scene Description (OpenUSD). This template showcases high-performance rendering, scene optimization,  live collaboration, and more. It is a great fit for interacting with large or complex 3D scenes.

By integrating advanced features such as instancing, optimization techniques, and new extension examples for planning, commenting, and reviewing, the USD Explorer Template simplifies the process of aggregating and examining large scenes. It offers a dual-mode UI, catering both to novices seeking ease of use and to advanced users requiring detailed scene manipulation capabilities.

### Use Cases

The USD Explorer Template is perfectly suited for:

- Visualizing complex industrial environments for planning and review.
- Collaborating on large-scale design projects in real-time.
- Building digital twins for industries to simulate and analyze real-world performance.

This template stands out by providing specialized tools for handling large scenes, making it an ideal choice for applications requiring detailed spatial analysis and collaborative review functionalities.

### Key Features

- **OpenUSD File Aggregation**: Seamlessly combine and manage multiple USD files in a unified scene.
- **Simple User Interface**: Intuitive interface designed for ease of use by non-specialized personnel.
- **Dual Mode Interface**: Toggle between simplified and advanced user interfaces based on user proficiency.
- **Easy Navigation**: Tools for smoothly navigating through large-scale scenes.
- **Annotation Tools**: Integrated tools for annotating and commenting within the scene for collaborative reviewing.
- **CAD Converter Import**: Directly import and convert CAD files into the OpenUSD format.
- **Live Collaboration**: Real-time collaboration tools allowing multiple users to view and edit scenes concurrently.
- **Content Library - Materials & Assets**: Extensive library of materials and assets for scene enhancement and realism.

## Usage

### Getting Started

To get started with the USD Explorer Template, ensure your development environment meets the prerequisites outlined in the top-level [**README**](../../../README.md#prerequisites-and-environment-setup).

> **NOTE:** Example commands should be executed in **powershell** in Windows and **terminal** in Linux.

#### Cloning the Repository

```bash
git clone https://github.com/NVIDIA-Omniverse/kit-app-template.git
cd kit-app-template
```

#### Create New Application

**Note for USD Explorer** : Some applications require setup extensions to function as intended. In the case of USD Explorer, the setup extension controls the configuration of the extensions within the application, their layout, and other settings. During Application configuration, you will be prompted for information about this extension.

> **NOTE:** Feel free to use default values for testing purposes.

**Linux:**
```bash
./repo.sh template new
```

**Windows:**
```powershell
.\repo.bat template new
```

> **NOTE:** If this is your first time running the `template new` tool, you'll be prompted to accept the Omniverse Licensing Terms.

Follow the prompt instructions:
- **? Select with arrow keys what you want to create:** Application
- **? Select with arrow keys your desired template:** USD Explorer
- **? Enter name of application .kit file [name-spaced, lowercase, alphanumeric]:** [set application name]
- **? Enter application_display_name:** [set application display name]
- **? Enter version:** [set app version]

*The application template you have selected requires a setup extension.
Setup Extension -> omni_usd_explorer_setup*
- **? Enter name of extension [name-spaced, lowercase, alphanumeric]:** [set extension name]
- **? Enter extension_display_name:** [set extension display name]
- **? Enter version:** [set extension version]

### Build and Launch
Note that the build step will build all applications contained in the `source` directory. Outside of initial experimentation, it is recommended that you build only the application you are actively developing.

#### Build your application using the provided build scripts:

**Linux:**
```bash
./repo.sh build
```
**Windows:**
```powershell
.\repo.bat build
```

 If you experience issues related to build, please see the [Usage and Troubleshooting](readme-assets/additional-docs/usage_and_troubleshooting.md) section for additional information.

#### Launch your application:

**Linux:**
```bash
./repo.sh launch
```
**Windows:**
```powershell
.\repo.bat launch
```

**? Select with arrow keys which App would you like to launch:** [Select the desired explorer application]

> **NOTE:** The initial startup may take a 5 to 8 minutes as shaders compile for the first time. After initial shader compilation, startup time will reduce dramatically.

![Launched USD Explorer](../../../readme-assets/usd_explorer_default_launch.png)

### Where to Go From Here
For more guidance on modifying the USD Explorer Template, visit the [Kit App Template Companion Tutorial - Extending Reference Applications](https://docs.omniverse.nvidia.com/kit/docs/kit-app-template/latest/docs/customize_reference_apps.html). This tutorial offers a step-by-step guide to help you understand the template's structure and customize it to suit your needs.

### Testing
Applications and their associated extensions can be tested using the `repo test` tooling provided. Each application template includes an initial test suite that can be run to verify the application's functionality.

> **NOTE:** Testing will only be run on applications and extensions within the build directory. **A successful build is required before testing.**

**Linux:**
```bash
./repo.sh test
```

**Windows:**
```powershell
.\repo.bat test
```

### Customization

#### Enable Extension
- On launch of the Application enable the developer bundle by adding the `--dev-bundle` or `-d` flag to the launch command.

    **Linux:**
    ```bash
    ./repo.sh launch --dev-bundle
    ```
    **Windows:**
    ```powershell
    .\repo.bat launch --dev-bundle
    ```
- From the running application select `Developer` > `Extensions`

- Browse and enable extensions of interest from the Extension Manager.
    - Enabling the extensions within the Extension Manager UI will allow you to try out the features of the extension in the currently running application.

    - To permanently add the extension to the application, you will need to add the extension to the `.kit` file. For example, adding the Layer View extension would require adding `omni.kit.widget.layers` to the dependencies section of the `.kit` file.

- For additional information on the Developer Bundle Extensions, refer to the [Developer Bundle Extensions](../../../readme-assets/additional-docs/developer_bundle_extensions.md) documentation.


#### Create Custom Extension

**Linux:**
```bash
./repo.sh template new
```

**Windows:**
```powershell
.\repo.bat template new
```

Follow the prompt instructions:
- **? Select with arrow keys what you want to create:** Extension
- **? Select with arrow keys your desired template:**: [choose extension template]
- **? Enter name of extension [name-spaced, lowercase, alphanumeric]:**: [set extension name]
- **? Enter extension_display_name:**: [set extension display name]
- **? Enter version:**: [set extension version]


#### Adding Extension to .kit File
**Importantly** For an extension to become a persistent part of an application, the extension will need to be added to the `.kit` file.

```toml
[dependencies]
"extension.name" = {}
```

#### Build with New Extensions
After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.

### Packaging and Deployment

For deploying your application, create a deployable package using the `package` command:

**Linux:**
```bash
./repo.sh package
```
**Windows:**
```powershell
.\repo.bat package
```

By default, the `package` command will name the package based on the `name` value contained in the repo.toml file at the root of the repository. **By default, this value is set to `kit-app-template`.** Modify this value to set a persistent package name for your application.

Alternatively, you can specify a package name using the `--name` flag:

**Linux:**
```bash
./repo.sh package --name <package_name>
```
**Windows:**
```powershell
.\repo.bat package --name <package_name>
```

This will bundle your application into a distributable format, ready for deployment on compatible platforms.

:warning: **Important Note for Packaging:** Because the packaging operation will package everything within the `source/` directory the package version will need to be set independently of a given `kit` file.  **The version is set within the `tools/VERSION.md` file.**

#### Launching a Package

Applications packaged using the `package` command can be launched using the `launch` command:

**Linux:**
```bash
./repo.sh launch --package <full-path-to-package>
```
**Windows:**
```powershell
.\repo.bat launch --package <full-path-to-package>
```

> **NOTE:** This behavior is not supported when packaging with the `--thin` flag.

### Containerization (Linux Only)

**Requires:** `Docker` and `NVIDIA Container Toolkit`

The packaging tooling provided by the Kit App Template also supports containerization of applications. This is especially useful for deploying headless services and streaming applications in a containerized environment.

To package your application as a container image, use the `--container` flag:

**Linux:**
```bash
./repo.sh package --container
```

You will be prompted to select a `.kit` file to serve as the application to launch via the container entrypoint script. This will dictate the behavior of your containerized application. 

For example, if you are containerizing an application for streaming, select the `{your-app-name}_streaming.kit` file to ensure the correct application configuration is launched within the container.

Similar to desktop packaging, the container option allows for specifying a package name using the `--name` flag to name the container image:

**Linux:**
```bash
./repo.sh package --container --name [container_image_name]
```

#### Launching a Container

Applications packaged as container images can be launched using the `launch` command:

**Linux:**
```bash
./repo.sh launch --container 
```

If only a single container image exists, it will launch automatically. If multiple container images exist, you will be prompted to select the desired container image to launch.

### Local Streaming

The UI-based template applications in this repository produce more than a single `.kit` file. For the USD Explorer template application, this includes `{your-app-name}_streaming.kit` which we will use for local streaming. This file inherits from the base application and adds necessary streaming components like `omni.kit.livestream.webrtc`. To try local streaming, you need a web client to connect to the streaming server.

#### 1. Clone Web Viewer Sample

The web viewer sample can be found [here](https://github.com/NVIDIA-Omniverse/web-viewer-sample)

```base
git clone https://github.com/NVIDIA-Omniverse/web-viewer-sample.git
```

Follow the instructions in the README to install the necessary dependencies.

#### 2. Modify the Web Viewer Sample

The Web Viewer Sample is configured by default to connect to the USD Viewer application template and includes web UI elements for sending API calls to a running Kit application. This is necessary for the Viewer template, which has limited functionality for driving application behavior directly. However, for the USD Explorer template, this messaging UI functionality isn't needed as the USD Explorer Template includes menus and other UI elements that can be interacted with directly.

When connecting the Web Viewer Sample to the USD Explorer application template, it is recommended to modify the source code. Make the following change to the web viewer sample:

**In `web-viewer-sample/src/App.tsx`**

- Change:
```typescript
import Window from './Window';
```

- To:
```typescript
import Window from './ViewportOnly';
```

#### 3. Start the streaming Kit Application

:warning: **Important**: Launching the streaming application with `--no-window` passes an argument directly to Kit allowing it to run without the main application window to prevent conflicts with the streaming client.

**Launch and stream a desktop application:**

**Linux:**
```bash
./repo.sh launch -- --no-window
```
**Windows:**
```powershell
.\repo.bat launch -- --no-window
```

Select the `{your-app-name}_streaming.kit` and wait for the application to start

**Launch and stream a containerized application:**

When streaming a containerized application, ensure that the containerized application was configured during packaging to launch a streaming application (e.g., `{your_app_name}_streaming.kit`).

**Linux:**
```bash
./repo.sh launch --container 
```

If only a single container image exists, it will launch automatically. If multiple container images exist, you will be prompted to select the desired container image to launch.

> **NOTE:** The `--no-window` flag is not required for containerized applications as it is the default launch behavior.

#### 4. Start the Streaming Client
```bash
npm run dev
```

In a Chromium-based browser, navigate to [http://localhost:5173/](http://localhost:5173/) and you should see the streaming client connect to the running Kit application.

![Streaming Explorer Image](../../../readme-assets/streaming_explorer.png)

## Additional Learning

- [Kit App Template Companion Tutorial](https://docs.omniverse.nvidia.com/kit/docs/kit-app-template/latest/docs/intro.html)
