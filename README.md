# The Idea

We are going to add Victoria 3 style revolutions and law passing but with Stellaris ethics and flavor. Metrics of success will be whether large empires splinter under ethic strain and whether internal politics and factions feel alive.

## Changes to Policy Passing

- Disable the instant policy passing
- Create an event that lets you choose which policy you'd like to try to pass
- You can only pass policies based on your government form. Dictatorships relies on your leader's ethics. Oligarchies rely on your council. Democracy relies on factions. 
- Whether or not you succeed at passing depends on faction support in your empire.
- Choosing a policy creates situation for passing the policy, with population support for the policy's ethic giving it positive progress and negative support detracting progress.
- Getting to 100 passes the policy.
- Getting to 0 blocks the policy of being passed for a decade.

## Feature for Revolutions

- Angry factions will create revolution situations for policies your ethics allow you to pass.
- At 100, they create a breakaway state in total war with you.
- Beginning the passing process of the policy they want prevents the revolution.

## Other thoughts

- What about policies you cannot pass due to ethics?

# Contribution Guide

This project relies on being familiar with Python and the command line.

This project uses a tool I made called Intemplator. Intemplator turns json blobs (eg. a blob for each ethic or policy), combines them with template files (eg a localisation file and an event file) to create final mod files without having to manually create a mod file for every single piece of content. This means that we can make tiny changes and instantly propograte them to hundreds of pieces of content. 

## Environment Setup

- Install python
- `git clone https://github.com/TNG-Modding/paradox-gamefiles-templatemaker.git`
- `cd paradox-gamefiles-templatemaker`
- `python setup.py install`
- Test that intemplator is installed by running `intemplator` in your terminal it should give you options
- `git clone https://github.com/TNG-Modding/stellaris-victoria-3-politics.git`
- `cd ./stellaris-victoria-3-politics/zintemplator`
- `intemplator go`. This should take the specs, run them through our templates, and create the files for our mod. 

## Submitting Your Changes

Create a new branch for your changes, and submit a pull request to master. You can ping me on Discord @thenextguy if you want to bring it to my attention.

## Creating your Own Content

The easiest way to create new content for the mod is to expand existing content in the specs files. For instance, copy a json blob about defensive wars and turn it into a different policy.

