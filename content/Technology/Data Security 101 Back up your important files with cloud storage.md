Title: Data Security 101: Back up your important files with cloud storage
Date: 2020-08-10 20:03
Slug: data-security-101-cloud-storage
Tags: online, security, cloud storage, files, backup, privacy
Category: Technology
Status: published

When you use a computer regularly, over time, you will accumulate lots of files and documents which are meaningful to you. It could be personal documents, digital products that you have downloaded and saved, research material, articles, and so on. But is all this data safe and secure? It would probably be very unpleasant if one day you lost all these files or if someone got access to them.

![Cloud][alex-machado-80sv993luki-unsplash]

_Photo by_ [_Alex Machado_](https://unsplash.com/@alexmachado?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) _on_ [_Unsplash_](https://unsplash.com/s/photos/cloud?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

These are the elements of data security that are important to consider:

- data redundancy: in the case of a computer failure you should still have access to an **up to date** backup of your files
- data privacy: other people cannot access your files unless you explicitly share them

Something else to consider is that you are likely using multiple devices: a desktop computer, a laptop, a tablet, a smartphone, and so on. Ideally, you would want easy access to your files on all your devices whenever you need it. That is what cloud-based automatic file syncing services allow you to do.

# Data Redundancy

Any computing device that you currently own will fail sooner or later. You could accidentally drop your laptop onto the ground, and it will break. Or it could fail over time due to normal wear and tear through no fault of your own. So you cannot rely on the storage of any physical device you own, no matter how high quality it is. If you do, you will eventually lose your files.

One option to resolve this issue is to manually take backups onto an external hard drive, optical disks, or other physical storage media. But this is a manual step, so it is not practical to do it frequently. And that external physical media is also subject to breaking eventually.

All **cloud storage** services aim to solve this problem. Once you set one up, it will automatically upload your files from a designated folder to the cloud. And if you connect a second or third device to it, they will download these files as well. So another benefit is that you can interchangeably access and work on them, without constant manual copying.

Problem solved, right?

# Data Privacy

The catch is that this potentially exposes your data to the company that stores it, the government (with the revelation of the [PRISM](<https://en.wikipedia.org/wiki/PRISM_(surveillance_program)>) surveillance program this is a real possibility). Or you could be collateral damage to any hackers who target that company. Most **cloud storage** solutions do not protect you from this.

The solution to this is called **zero-knowledge encryption**. In this case, the data gets **encrypted** on your computer before it gets uploaded to the cloud. The uploaded files do not make any sense whatsoever without the key (the password), which you have used to encrypt them. It is just a meaningless pile of data without it. The cloud storage service does not have access to this key.

There are not that many services that offer such a proper level of privacy. The most popular ones are [Sync.com](https://www.sync.com/?_sync_refer=964cb40), [pCloud](https://www.pcloud.com/eu), and [MEGA](https://mega.nz/startpage). I use [Sync.com](https://www.sync.com/?_sync_refer=964cb40), so that is what I can most recommend, but feel free to check out the other options as well.

# Setting Up

Once you have chosen a provider, you will need to:

- register account with a strong password
- install the application on the computer where most of your data lives
- choose the folder (or folders) which you want to back up
- wait for the initial sync to happen
- install on additional devices as needed

One caveat with **zero-knowledge encryption** is that you will need to remember your password, or you may not be able to download your data anymore. I highly recommend that you add it to a [password manager]({filename}/Technology/Online_Security_101_How_to_secure_your_online_accounts.md).

Once you have your application going on your computer, it might take a long time for it to upload all your files to the cloud. It depends on how much you are backing up and the upload speed of your internet connection. Also, it will take time to fully download on a second device, if you need to do that. But it’s done automatically, and it will be kept up to date with new files automatically and painlessly.

On smartphones, it won’t sync all your data, it will just get the specific file that you wish to open on-demand.

# Conclusion

I hope that I have persuaded you to set up an automated **cloud storage** backup for your files. And especially to use a private service if at all possible, but any solution is better than nothing. For specific instructions, you can look at the website of your chosen solution, I’ve only covered a general overview here.

Now go on and back up your data!

[alex-machado-80sv993luki-unsplash]: {static}/images/alex-machado-80sv993lUKI-unsplash.jpg "Cloud in the sky"
