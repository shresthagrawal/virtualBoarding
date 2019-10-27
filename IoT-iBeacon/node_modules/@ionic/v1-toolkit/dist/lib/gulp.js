"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const format_1 = require("@ionic/cli-framework/utils/format");
const promise_1 = require("@ionic/cli-framework/utils/promise");
const chalk_1 = require("chalk");
const Debug = require("debug");
const path = require("path");
const log_1 = require("./log");
const debug = Debug('ionic:v1-toolkit:lib:gulp');
let _gulpInst;
async function loadGulp() {
    if (!_gulpInst) {
        const gulpFilePath = path.resolve('gulpfile.js');
        debug(`Using gulpfile: ${gulpFilePath}`);
        try {
            const gulpPath = require.resolve('gulp');
            debug(`Using gulp: ${gulpPath}`);
            _gulpInst = require(gulpPath);
        }
        catch (e) {
            if (e.code !== 'MODULE_NOT_FOUND') {
                throw e;
            }
            throw new Error(chalk_1.default.red(`Cannot find module 'gulp'`));
        }
        try {
            require(gulpFilePath); // requiring the gulp file sets up the gulp instance with local gulp task definitions
        }
        catch (e) {
            if (e.code !== 'MODULE_NOT_FOUND') {
                throw e;
            }
            throw new Error(`Error in module: ${chalk_1.default.bold(format_1.prettyPath(gulpFilePath))}:\n` +
                chalk_1.default.red(e.stack ? e.stack : e));
        }
        debug('Loaded gulp tasks: %o', _gulpInst.tasks);
    }
    return _gulpInst;
}
exports.loadGulp = loadGulp;
async function hasTask(name) {
    try {
        const gulp = await loadGulp();
        return gulp.hasTask(name);
    }
    catch (e) {
        process.stderr.write(`${log_1.timestamp()} Cannot load gulp: ${String(e)}\n`);
    }
    return false;
}
exports.hasTask = hasTask;
async function runTask(name) {
    if (!(await hasTask(name))) {
        process.stderr.write(`${log_1.timestamp()} Cannot run ${chalk_1.default.cyan(name)} task: missing in ${chalk_1.default.bold('gulpfile.js')}\n`);
        return;
    }
    try {
        const gulp = await loadGulp();
        const boundStart = gulp.start.bind(gulp);
        const gulpStart = promise_1.promisify(boundStart);
        process.stdout.write(`${log_1.timestamp()} Invoking ${chalk_1.default.cyan(name)} gulp task.\n`);
        await gulpStart(name);
    }
    catch (e) {
        process.stderr.write(`${log_1.timestamp()} Cannot run ${chalk_1.default.cyan(name)} task: ${String(e)}\n`);
    }
}
exports.runTask = runTask;
