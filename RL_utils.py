import os
import matplotlib.pyplot as plt
import numpy as np
from JSAnimation import IPython_display
from matplotlib import animation
import cv2
import imageio
import mpld3
import scipy.misc

def plot_movie_js2(enc_array,image_array,save=None):
    #Shows encoding and frames
    fig = plt.figure(figsize=(10,3), dpi=72)
    ax1 = fig.add_subplot(2, 2, 1)
    plt.title('Visual Encoding', fontsize=15)
    plt.axis('off')
    im = plt.imshow(enc_array[0][:8,:],vmin=-1,vmax=25)
    ax2 = fig.add_subplot(2, 2, 3)
    plt.title('Vector Encoding', fontsize=15)
    plt.axis('off')
    im2 = plt.imshow(enc_array[0][8:,:],vmin=-1,vmax=25)
    ax3 = fig.add_subplot(1, 2, 2)
    im3 = plt.imshow(image_array[0])
    plt.axis('off')
    
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=10, metadata=dict(artist='Me'), bitrate=1800)

    def animate(i):
        im.set_array(enc_array[i][:8,:])
        im2.set_array(enc_array[i][8:,:])
        im3.set_array(image_array[i])
        return (im,)
    
    anim = animation.FuncAnimation(fig, animate, frames=len(image_array))

    display(IPython_display.display_animation(anim))
    if save!=None:
        anim.save(save, writer=writer)
        
def save_movie_js2(enc_array,image_array,save=None):
    #dpi = 72.0
    #xpixels, ypixels = image_array[0].shape[0], image_array[0].shape[1]
    fig = plt.figure(figsize=(10,3), dpi=72)
    ax1 = fig.add_subplot(2, 2, 1)
    plt.title('Visual Encoding', fontsize=15)
    plt.axis('off')
    im = plt.imshow(enc_array[0][:8,:],vmin=-1,vmax=25)
    ax2 = fig.add_subplot(2, 2, 3)
    plt.title('Vector Encoding', fontsize=15)
    plt.axis('off')
    im2 = plt.imshow(enc_array[0][8:,:],vmin=-1,vmax=25)
    ax3 = fig.add_subplot(1, 2, 2)
    im3 = plt.imshow(image_array[0])
    plt.axis('off')

    for i in range(enc_array.shape[0]):
        im.set_array(enc_array[i][:8,:])
        im2.set_array(enc_array[i][8:,:])
        im3.set_array(image_array[i])
        #plt.savefig(path+save+'/img'+str(i).zfill(4)+'.png', bbox_inches='tight')
        plt.savefig(save+'/img'+str(i)+'.png', bbox_inches='tight')
        
def plot_movie_jsInfo(enc_array,image_array,acts,vals,rews,save=None):
    
    def getImage(act,num):
        if act==0:
            return stand
        if num==0:
            if act==1:
                return up
            if act==2:
                return down
        if num==1:
            if act==1:
                return turn_l
            if act==2:
                return turn_r
        if num==2 and act==1:
            return jump
        if num==3:
            if act==1:
                return right
            if act==2:
                return left
    
    jump = imageio.imread('./symbols/jump.png')
    left = imageio.imread('./symbols/arrow-left.png')
    right = imageio.imread('./symbols/arrow_right.png')
    down = imageio.imread('./symbols/down-arrow.png')
    up = imageio.imread('./symbols/up-arrow.png')
    turn_l = imageio.imread('./symbols/turn-left.png')
    turn_r = imageio.imread('./symbols/turn-right.png')
    stand = imageio.imread('./symbols/Stand.png')
    
    fig = plt.figure(figsize=(10,3), dpi=72)
    ax1 = fig.add_subplot(2, 2, 1)
    plt.axis('off')
    if not isinstance(enc_array,list):
        im = plt.imshow(enc_array[0][:8,:],vmin=-1,vmax=25)
        plt.title('Visual Encoding', fontsize=15)
    else:
        icaLen = enc_array[0][0].shape[0]
        im = plt.imshow(enc_array[0][0].reshape(1,icaLen),vmin=-1,vmax=25)
        plt.title('Visual Encoding - ICs', fontsize=15)
    ax2 = fig.add_subplot(2, 2, 3)
    plt.axis('off')
    if not isinstance(enc_array,list):
        im2 = plt.imshow(enc_array[0][8:,:],vmin=-1,vmax=25)
        plt.title('Vector Encoding', fontsize=15)
    else:
        im2 = plt.imshow(enc_array[1][0].reshape(1,icaLen),vmin=-1,vmax=25)
        plt.title('Vector Encoding - ICs', fontsize=15)
    ax4 = fig.add_subplot(1, 2, 2)
    im4 = plt.imshow(image_array[0])
    plt.axis('off')
    ax3 = fig.add_subplot(6, 2, 2)
    im3 = plt.text(0.2,0.1,"R: "+str(rews[0])+' V: '+str(vals[0]), fontsize=15,color='white',
                   bbox=dict(facecolor='blue', alpha=0.5))
    plt.axis('off')
    
    ax5 = fig.add_subplot(4, 10, 10)
    im5 = plt.imshow(getImage(acts[0][0][0],0))
    plt.axis('off')
    ax6 = fig.add_subplot(4, 10, 20)
    im6 = plt.imshow(getImage(acts[0][0][1],1))
    plt.axis('off')
    ax7 = fig.add_subplot(4, 10, 30)
    im7 = plt.imshow(getImage(acts[0][0][2],2))
    plt.axis('off')
    ax8 = fig.add_subplot(4, 10, 40)
    im8 = plt.imshow(getImage(acts[0][0][3],3))
    plt.axis('off')
    
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=10, metadata=dict(artist='Me'), bitrate=1800)
    

    
    def animate(i):
        if not isinstance(enc_array,list):
            im.set_array(enc_array[i][:8,:])
            im2.set_array(enc_array[i][8:,:])
        else:
            im.set_array(enc_array[0][i].reshape(1,icaLen))
            im2.set_array(enc_array[1][i].reshape(1,icaLen))
        im3.set_text("R: "+str(rews[i])[:3]+' V: '+str(vals[i][0][0])[:4])
        im4.set_array(image_array[i])
        im5.set_array(getImage(acts[i][0][0],0))
        im6.set_array(getImage(acts[i][0][1],1))
        im7.set_array(getImage(acts[i][0][2],2))
        im8.set_array(getImage(acts[i][0][3],3))
        return (im,)

    anim = animation.FuncAnimation(fig, animate, frames=len(image_array))
    display(IPython_display.display_animation(anim))
    if save!=None:
        anim.save(save, writer=writer)

def save_movie_jsInfo(enc_array,image_array,acts,vals,rews,save=None):
    
    def getImage(act,num):
        if act==0:
            return stand
        if num==0:
            if act==1:
                return up
            if act==2:
                return down
        if num==1:
            if act==1:
                return turn_l
            if act==2:
                return turn_r
        if num==2 and act==1:
            return jump
        if num==3:
            if act==1:
                return right
            if act==2:
                return left
    
    jump = imageio.imread('./symbols/jump.png')
    left = imageio.imread('./symbols/arrow-left.png')
    right = imageio.imread('./symbols/arrow_right.png')
    down = imageio.imread('./symbols/down-arrow.png')
    up = imageio.imread('./symbols/up-arrow.png')
    turn_l = imageio.imread('./symbols/turn-left.png')
    turn_r = imageio.imread('./symbols/turn-right.png')
    stand = imageio.imread('./symbols/Stand.png')
    
    fig = plt.figure(figsize=(10,3), dpi=72)
    ax1 = fig.add_subplot(2, 2, 1)
    plt.axis('off')
    if not isinstance(enc_array,list):
        im = plt.imshow(enc_array[0][:8,:],vmin=-1,vmax=25)
        plt.title('Visual Encoding', fontsize=15)
    else:
        icaLen = enc_array[0][0].shape[0]
        im = plt.imshow(enc_array[0][0].reshape(1,icaLen),vmin=-1,vmax=25)
        plt.title('Visual Encoding - ICs', fontsize=15)
    ax2 = fig.add_subplot(2, 2, 3)
    plt.axis('off')
    if not isinstance(enc_array,list):
        im2 = plt.imshow(enc_array[0][8:,:],vmin=-1,vmax=25)
        plt.title('Vector Encoding', fontsize=15)
    else:
        im2 = plt.imshow(enc_array[1][0].reshape(1,icaLen),vmin=-1,vmax=25)
        plt.title('Vector Encoding - ICs', fontsize=15)
    ax4 = fig.add_subplot(1, 2, 2)
    im4 = plt.imshow(image_array[0])
    plt.axis('off')
    ax3 = fig.add_subplot(6, 2, 2)
    im3 = plt.text(0.2,0.1,"R: "+str(rews[0])+' V: '+str(vals[0]), fontsize=15,color='white',
                   bbox=dict(facecolor='blue', alpha=0.5))
    plt.axis('off')
    
    ax5 = fig.add_subplot(4, 10, 10)
    im5 = plt.imshow(getImage(acts[0][0][0],0))
    plt.axis('off')
    ax6 = fig.add_subplot(4, 10, 20)
    im6 = plt.imshow(getImage(acts[0][0][1],1))
    plt.axis('off')
    ax7 = fig.add_subplot(4, 10, 30)
    im7 = plt.imshow(getImage(acts[0][0][2],2))
    plt.axis('off')
    ax8 = fig.add_subplot(4, 10, 40)
    im8 = plt.imshow(getImage(acts[0][0][3],3))
    plt.axis('off')
    
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=10, metadata=dict(artist='Me'), bitrate=1800)
    
    if isinstance(enc_array,list):
        a_len = rews.shape[0]
    else:
        a_len = enc_array.shape[0]
    
    for i in range(a_len):
        if not isinstance(enc_array,list):
            im.set_array(enc_array[i][:8,:])
            im2.set_array(enc_array[i][8:,:])
        else:
            im.set_array(enc_array[0][i].reshape(1,icaLen))
            im2.set_array(enc_array[1][i].reshape(1,icaLen))
        im3.set_text("R: "+str(rews[i])[:3]+' V: '+str(vals[i][0][0])[:4])
        im4.set_array(image_array[i])
        im5.set_array(getImage(acts[i][0][0],0))
        im6.set_array(getImage(acts[i][0][1],1))
        im7.set_array(getImage(acts[i][0][2],2))
        im8.set_array(getImage(acts[i][0][3],3))
        plt.savefig(save+'/img'+str(i).zfill(4)+'.png', bbox_inches='tight')

def plot_movie_js3(enc_array,image_array,cluster, save=None):
    #Plot Encodings and frames + information about which cluster the frame is in
    fig = plt.figure(figsize=(10,3), dpi=72)
    ax1 = fig.add_subplot(2, 2, 1)
    plt.axis('off')
    im = plt.imshow(enc_array[0][:8,:],vmin=-1,vmax=25)
    plt.title('Visual Encoding', fontsize=15)
    ax2 = fig.add_subplot(2, 2, 3)
    plt.axis('off')
    im2 = plt.imshow(enc_array[0][8:,:],vmin=-1,vmax=25)
    plt.title('Vector Encoding', fontsize=15)
    ax4 = fig.add_subplot(1, 2, 2)
    plt.axis('off')
    im4 = plt.imshow(image_array[0])
    ax3 = fig.add_subplot(6, 2, 2)
    im3 = plt.text(0.3,0.1,'Cluster ' + str(cluster[0]), fontsize=20,color='white',bbox=dict(facecolor='blue', alpha=0.5))
    plt.axis('off')
    
    
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=10, metadata=dict(artist='Me'), bitrate=1800)

    def animate(i):
        im.set_array(enc_array[i][:8,:])
        im2.set_array(enc_array[i][8:,:])
        im3.set_text('Cluster ' + str(cluster[i]))
        im4.set_array(image_array[i])
        return (im,)

    anim = animation.FuncAnimation(fig, animate, frames=len(image_array))
    display(IPython_display.display_animation(anim))
    if save!=None:
        anim.save(save, writer=writer)

def plot_actions(act):
    fig = plt.figure(figsize=(10,7))
    fig.suptitle('Distribution of Actions', fontsize=20)
    ax1 = fig.add_subplot(2, 2, 1)
    plt.hist(act[:,0,0],bins=np.linspace(-0.5,2.5,4))
    plt.title('Move Forward/Back', fontsize=15)
    plt.xticks(np.arange(3),['Stand','Forward','Back'], fontsize=13)
    ax2 = fig.add_subplot(2, 2, 2)
    plt.hist(act[:,0,1],bins=np.linspace(-0.5,2.5,4))
    plt.title('Camera', fontsize=15)
    plt.xticks(np.arange(3),['Straight','Left','Right'], fontsize=13)
    ax3 = fig.add_subplot(2, 2, 3)
    plt.hist(act[:,0,2],bins=np.linspace(-0.5,1.5,3))
    plt.title('Jump', fontsize=15)
    plt.xticks(np.arange(2),['Stand','Jump'], fontsize=13)
    ax4 = fig.add_subplot(2, 2, 4)
    plt.hist(act[:,0,3],bins=np.linspace(-0.5,2.5,4))
    plt.title('Move Left/Right', fontsize=15)
    plt.xticks(np.arange(3),['Stand','Right','Left'], fontsize=13)
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    return fig

def correlate(enc,val,num=0,normalize=False):
    corrs = []
    v = val#[:,0,num]
    if normalize:
        v = (v - np.mean(v)) /  np.std(v)
    for i in range(enc.shape[-1]):
        e = enc[:,i]
        if normalize:
            e = (e - np.mean(e)) / (np.std(e) * len(e))
        #corr = np.correlate(e,v)
        corr = np.corrcoef(e,v)[0,1]
        corrs.append(float(corr))
    return np.array(corrs)