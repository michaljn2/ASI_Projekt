"""ASI file for ensuring the package is executable
as `asi` and `python -m asi`
"""
import importlib
from pathlib import Path

from kedro.framework.cli.utils import KedroCliError, load_entry_points
from kedro.framework.project import configure_project


def _find_run_command(package_name):
    try:
        project_cli = importlib.import_module(f"{package_name}.cli")
        # fail gracefully if cli.py does not exist
    except ModuleNotFoundError as exc:
        if f"{package_name}.cli" not in str(exc):
            raise
        plugins = load_entry_points("project")
        run = _find_run_command_in_plugins(plugins) if plugins else None
        if run:
            # use run command from installed plugin if it exists
            return run
        # use run command from `kedro.framework.cli.project`
        from kedro.framework.cli.project import run

        return run
    # fail badly if cli.py exists, but has no `cli` in it
    if not hasattr(project_cli, "cli"):
        raise KedroCliError(f"Cannot load commands from {package_name}.cli")
    return project_cli.run


def _find_run_command_in_plugins(plugins):
    for group in plugins:
        if "run" in group.commands:
            return group.commands["run"]


def main(*args, **kwargs):
    package_name = Path(__file__).parent.name
    configure_project(package_name)
    run = _find_run_command(package_name)
    run(*args, **kwargs)

    st.title("Rain prediction app")

    minTemp_slider = st.slider("Min temperature", min_value=-10, max_value=50, step=0.5)
    maxTemp_slider = st.slider("Max temperature", min_value=-10, max_value=50, step=0.5)
    rainfall_slider = st.slider("Rainfall", min_value=0, max_value=400, step=1)
    evaporation_slider = st.slider("Evaporation", min_value=0, max_valute=150, step=1)
    sunshine_slider = st.slider("Sunshine", min_value=0, max_value=15, step=1)
    windGustSpeed_slider = st.slider("Wind gust speed", min_value=0, max_value=140, step=1)
    windSpeed9am_slider = st.slider("Wind speed at 9am", min_value=0, max_value=140, step=1)
    windSpeed3pm_slider = st.slider("Wind speed at 3am", min_value=0, max_value=140, step=1)
    humidity9am_slider = st.slider("Humidity at 9am", min_value=0, max_value=100, step=1)
    humidity3pm_slider = st.slider("Humidity at 3pm", min_value=0, max_value=100, step=1)
    pressure9am_slider = st.slider("Pressure at 9am", min_value=970, max_value=1050, step=0.5)
    pressure3pm_slider = st.slider("Pressure at 3pm", min_value=970, max_value=1050, step=0.5)
    cloud9am_slider = st.slider("Cloudiness at 9am", min_value=0, max_value=10, step=1)
    cloud3pm_slider = st.slider("Cloudiness at 3pm", min_value=0, max_value=10, step=1)
    temp9am_slider = st.slider("Temperature at 9am", min_value=-10, max_value=50, step=1)
    temp3pm_slider = st.slider("Temperature at 3pm", min_value=-10, max_value=50, step=1)




if __name__ == "__main__":
    main()